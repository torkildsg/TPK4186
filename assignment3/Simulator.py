"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Schedule import Schedule
from Plant import Plant
from Event import Event
from Task import Task
from Buffer import Buffer

class Simulator:
    def __init__(self, plant):
        self.plant = plant
        self.executionTime = dict() # Key: batchCode, value: total time for all tasks
        self.execution = []
        self.eventNumber = 0
    
    def getExecution(self):
        return self.execution
    
    def getExecutionTime(self):
        return self.executionTime
    
    # Må legge til:
    # Når en maskin er opptatt, blir en schdeuling satt på vent, og schdulet igjen senere...
    def simulationLoop(self, schedule):
        self.execution = []
        firstTask = schedule.getPlant().getFirstTask() # Her skal det være event... ikke task?
        schedule.scheduleBatchToTask(firstTask)

        while not schedule.isScheduleEmpty(): 
            event = schedule.popFirstEvent()
            if self.executeEvent(event, schedule):
                self.execution.append(event)
            else: 
                continue# Hvis executevent returnerte True, append
            

    def executeEvent(self, thisEvent, schedule):
        self.currentDate = thisEvent.getDate()
        thisBatch = thisEvent.getBatch()
        thisTask = thisEvent.getTask()
        outgoingBuffer = thisTask.getFirstOfOutgoingBuffers()
        incomingBuffer = thisTask.getFirstOfIncomingBuffers()
        thisBuffer = thisEvent.getBuffer()

        if thisEvent.getType() == Event.BATCH_TO_TASK:
            if not incomingBuffer.isEmpty() and thisTask.getName() != 'End':
                executed = self.executeBatchToTask(thisEvent, thisBuffer, thisBatch, thisTask, schedule)
                schedule.scheduleBatchToBuffer(outgoingBuffer)  # Schedule the batch into the outputbuffer
                return executed
            

        elif thisEvent.getType() == Event.BATCH_TO_BUFFER:
            executed = self.executeBatchToBuffer(outgoingBuffer, thisBatch, schedule)
            if not incomingBuffer.isEmpty() and thisTask.getName() != 'End':
                schedule.scheduleBatchToTask(thisTask) # Schedule a new batch into this task
            if not outgoingBuffer.isEmpty() and outgoingBuffer.getTargetTask().getName() != 'End':
                schedule.scheduleBatchToTask(outgoingBuffer.getTargetTask()) # Schedule a new batch into the next task
            return executed


    def executeBatchToTask(self, thisEvent, thisBuffer, thisBatch, thisTask, schedule):
        #if thisTask.getName() != 'End':
        duration = self.plant.taskServesBatch(thisBatch, thisTask)
        if duration:
            thisTask.setHoldingBatch(thisBatch)
            if not thisBatch.getBatchCode() in self.executionTime.keys():
                self.executionTime[thisBatch.getBatchCode()] = float(duration)
            else:
                self.executionTime[thisBatch.getBatchCode()] += float(duration)
            return True
        else: 
            #schedule.decreaseEventNum() # Funker ikke, indekserer feil
            #schedule.decreaseCurrentDate()
            # Må lage et nytt event med den batchen, og legge det til i sc
            #schedule.scheduleBatchToTask(thisTask)
            return False
    

    def executeBatchToBuffer(self, outgoingBuffer, thisBatch, schedule):
        sourceTask = outgoingBuffer.getSourceTask()
        targetTask = outgoingBuffer.getTargetTask() 

        if outgoingBuffer.getAvailableCap() >= thisBatch.getNumOfWafers():
            sourceTask.batchIsDone() # Removes the batch that the task holds, and sets the Task's state to idle
            self.plant.enqueueBatchIntoBuffer(thisBatch, outgoingBuffer)
            return True
        else:
            #schedule.decreaseEventNum()
            #schedule.decreaseCurrentDate() 
            schedule.scheduleBatchToBuffer(outgoingBuffer)
            return False


