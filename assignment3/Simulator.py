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
        schedule.scheduleBufferToTask(firstTask)

        while not schedule.isScheduleEmpty(): 
            event = schedule.popFirstEvent()
            if self.executeEvent(event, schedule):
                self.execution.append(event)
            else: 
                continue# Hvis executevent returnerte True, append
            

    def executeEvent(self, event, schedule):
        self.currentDate = event.getDate()
        thisBatch = event.getBatch()

        if event.getType() == Event.BUFFER_TO_TASK:
            targetTask = event.getTask()
            thisBuffer = event.getBuffer()
            sourceTask = thisBuffer.getSourceTask()
            nextBuffer = targetTask.getFirstOfOutgoingBuffers()
            task = thisBuffer.getTargetTask()

            if not thisBuffer.isEmpty() and sourceTask.getName() != 'End':
                executed = self.executeBatchToTask(event, thisBuffer, thisBatch, targetTask, schedule)
                schedule.scheduleTaskToBuffer(nextBuffer)  # Schedule the batch into the outputbuffer
                if not self.plant.getFirstTask().getFirstOfIncomingBuffers().isEmpty():
                    schedule.scheduleBufferToTask(self.plant.getFirstTask())
                return executed

        elif event.getType() == Event.TASK_TO_BUFFER:

            thisTask = event.getTask()
            targetBuffer = thisTask.getFirstOfOutgoingBuffers()
            sourceBuffer = thisTask.getFirstOfIncomingBuffers()
            nextTask = targetBuffer.getTargetTask()

            executed = self.executeBatchToBuffer(targetBuffer, thisBatch, schedule)
            if not targetBuffer.isEmpty() and targetBuffer.getTargetTask().getName() != 'End':
                schedule.scheduleBufferToTask(nextTask) # Schedule a new batch into the next task
            return executed


    def executeBatchToTask(self, event, buffer, batch, task, schedule):
        #if thisTask.getName() != 'End':
        duration = self.plant.taskServesBatch(batch, task)
        if duration:
            task.setHoldingBatch(batch)
            if not batch.getBatchCode() in self.executionTime.keys():
                self.executionTime[batch.getBatchCode()] = float(duration)
            else:
                self.executionTime[batch.getBatchCode()] += float(duration)
            return True
        else: 
            #schedule.decreaseEventNum() # Funker ikke, indekserer feil
            #schedule.decreaseCurrentDate()
            # Må lage et nytt event med den batchen, og legge det til i sc
            #schedule.scheduleBufferToTask(thisTask)
            return False
    

    def executeBatchToBuffer(self, buffer, batch, schedule):
        sourceTask = buffer.getSourceTask()
        targetTask = buffer.getTargetTask() 

        if buffer.getAvailableCap() >= batch.getNumOfWafers():
            sourceTask.batchIsDone() # Removes the batch that the task holds, and sets the Task's state to idle
            self.plant.enqueueBatchIntoBuffer(batch, buffer)
            return True
        else:
            #schedule.decreaseEventNum()
            #schedule.decreaseCurrentDate() 
            #schedule.scheduleTaskToBuffer(outgoingBuffer) # Ifølge S skal denne ikke schedules
            return False


