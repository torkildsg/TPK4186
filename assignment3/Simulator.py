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
    
    def simulationLoop(self, schedule):
        self.execution = []
        firstTask = schedule.getPlant().getFirstTask() # Her skal det være event... ikke task?
        schedule.scheduleBatchToTask(firstTask)

        while not schedule.isScheduleEmpty(): 
            #print(schedule.getSchedule())
            event = schedule.popFirstEvent()
            self.execution.append(event)
            self.executeEvent(event, schedule)
        
        #print("Schedule after simulation: " + str(schedule.getSchedule()))
        #print("Execution: " + str(self.getExecution()))
        #print(self.getExecutionTime())
    
    def executeEvent(self, thisEvent, schedule):
        self.currentDate = thisEvent.getDate()
        thisBatch = thisEvent.getBatch()
        thisTask = thisEvent.getTask()
        outgoingBuffer = thisTask.getFirstOfOutgoingBuffers()
        incomingBuffer = thisTask.getFirstOfIncomingBuffers()
        thisBuffer = thisEvent.getBuffer()
    
        #print(incomingBuffer.getQueueOfBatches())

        if thisEvent.getType() == Event.BATCH_TO_TASK:
            if not incomingBuffer.isEmpty() and thisTask.getName() != 'End':
                self.executeBatchToTask(thisEvent, thisBuffer, thisBatch, thisTask, schedule)
                schedule.scheduleBatchToBuffer(outgoingBuffer)

        elif thisEvent.getType() == Event.BATCH_TO_BUFFER:
            self.executeBatchToBuffer(outgoingBuffer, thisBatch, schedule)
            if not incomingBuffer.isEmpty() and thisTask.getName() != 'End':
                schedule.scheduleBatchToTask(thisTask)
            if not outgoingBuffer.isEmpty() and outgoingBuffer.getTargetTask().getName() != 'End':
                schedule.scheduleBatchToTask(outgoingBuffer.getTargetTask())


        
        """print(str(thisTask.getName()) + " incoming buffer hold the batches:")
        for t in thisTask.getFirstOfIncomingBuffers().getQueueOfBatches():
            print("Batchcode #" + str(t.getBatchCode()))
        print('\n')"""

        """print(str(targetTask.getName()) + " incoming buffer hold the batches:")
        for s in targetTask.getFirstOfIncomingBuffers().getQueueOfBatches():
            print("Batchcode #" + str(s.getBatchCode()))
        print('\n')"""

    def executeBatchToTask(self, thisEvent, thisBuffer, thisBatch, thisTask, schedule):
        
        
         # set alle states
        if thisTask.getName() != 'End':
            duration = self.plant.taskServesBatch(thisBatch, thisTask)
            thisTask.setHoldingBatch(thisBatch)
            if not thisBatch.getBatchCode() in self.executionTime.keys():
                self.executionTime[thisBatch.getBatchCode()] = float(duration)
            else:
                self.executionTime[thisBatch.getBatchCode()] += float(duration)
            # Schedule the batch into the outputbuffer
            """nextBuffer = thisTask.getFirstOfOutgoingBuffers()
            schedule.scheduleBatchToBuffer(nextBuffer)"""
            # Schedule a new batch into this task
            """if not thisTask.getFirstOfIncomingBuffers().isEmpty() and thisTask.getName() != 'End':
                schedule.scheduleBatchToTask(thisTask)"""
        else: return False
        
        #print(str(thisTask.getName()) + " now holds the batch #" + str(thisTask.getHoldingBatch().getBatchCode()) + '\n')
    
    def executeBatchToBuffer(self, outgoingBuffer, thisBatch, schedule):
        sourceTask = outgoingBuffer.getSourceTask()
        targetTask = outgoingBuffer.getTargetTask()

        if outgoingBuffer.getAvailableCap() >= thisBatch.getNumOfWafers():
            sourceTask.batchIsDone() # Removes the batch that the task holds, and sets the Task's state to idle
            self.plant.enqueueBatchIntoBuffer(thisBatch, outgoingBuffer)

            # Nå kan du schedule en NY batch til tasken som forrige buffer kom fra, samt schdule batch til neste Task
            """if not targetTask.getFirstOfIncomingBuffers().isEmpty() and targetTask.getName() != 'End':
                schedule.scheduleBatchToTask(targetTask)
            """



