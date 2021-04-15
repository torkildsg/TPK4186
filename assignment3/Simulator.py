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
        self.numOfIterationsInQueue = dict() # Skal vi bruke denne?
        self.eventNumber = 0

    def getNumOfIterationsInQueue(self): # Skal vi bruke denne?
        return self.numOfIterationsInQueue

    def getExecution(self):
        return self.execution
    
    def getExecutionTime(self):
        return self.executionTime
    
    def simulationLoop(self, schedule):
        self.execution = []
        firstTask = schedule.getPlant().getFirstTask() 
        schedule.scheduleBufferToTask(firstTask)

        while not schedule.isCurrentScheduleEmpty(): 
            event = schedule.popFirstEvent()
            if self.executeEvent(event, schedule):
                self.execution.append(event)
            else: 
                continue

    """def MonteCarloSimulation(self, numberOfClients, numberOfExecutions):
        terminationDates = []
        for index in range(0, numberOfExecutions):
            self.SimulationLoop(numberOfClients)
            terminationDates.append(self.currentDate)
        return terminationDates"""

    def simulationLoopForOptimizer(self, schedule, policyCombination):
        self.execution = []
        schedule.currentSchedule = []
        plant = schedule.getPlant()
        firstTask = plant.getFirstTask() 
        schedule.scheduleBufferToTask(firstTask)
        lastBatch = plant.getStartBuffer().getLastBatchInQueue()
        endBuffer = plant.getEndBuffer()

        while lastBatch not in endBuffer and not schedule.isCurrentScheduleEmpty():
            event = schedule.popFirstEvent()
            if self.executeEventForOptimizer(event, schedule):
                self.execution.append(event)
                for index, machine in enumerate(plant.getAllMachines(), 0):
                    plant.runMachinePolicy(self, schedule, machine, policyCombination[index])
            else: 
                continue
    
    def executeEventForOptimizer(self, event, schedule):
        self.currentDate = event.getDate()
        thisBatch = event.getBatch()

        if event.getType() == Event.BUFFER_TO_TASK:
            targetTask = event.getTask()
            thisBuffer = event.getBuffer()
            sourceTask = thisBuffer.getSourceTask()
            nextBuffer = targetTask.getFirstOfOutgoingBuffers()
            task = thisBuffer.getTargetTask()

            if not thisBuffer.isEmpty() and sourceTask.getName() != 'End':
                executed = self.executeBufferToTask(event, thisBuffer, thisBatch, targetTask, schedule)
                schedule.scheduleTaskToBuffer(nextBuffer)  # Schedule the batch into the outputbuffer
                
                """if len(thisBuffer.getQueueOfBatches()) > 0:
                    schedule.scheduleBufferToTask(thisBuffer.getTargetTask())
                """
                return executed
        
        elif event.getType() == Event.TASK_TO_BUFFER:

            thisTask = event.getTask()
            targetBuffer = thisTask.getFirstOfOutgoingBuffers()
            sourceBuffer = thisTask.getFirstOfIncomingBuffers()
            nextTask = targetBuffer.getTargetTask()

            executed = self.executeTaskToBuffer(targetBuffer, thisBatch, schedule)
            """if targetBuffer.getTargetTask().getName() != 'End':
                schedule.scheduleBufferToTask(nextTask) # Schedule a new batch into the next task
            """
            return executed

            
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
                executed = self.executeBufferToTask(event, thisBuffer, thisBatch, targetTask, schedule)
                schedule.scheduleTaskToBuffer(nextBuffer)  # Schedule the batch into the outputbuffer
                
                if len(thisBuffer.getQueueOfBatches()) > 0:
                    schedule.scheduleBufferToTask(thisBuffer.getTargetTask())

                return executed

        elif event.getType() == Event.TASK_TO_BUFFER:

            thisTask = event.getTask()
            targetBuffer = thisTask.getFirstOfOutgoingBuffers()
            sourceBuffer = thisTask.getFirstOfIncomingBuffers()
            nextTask = targetBuffer.getTargetTask()

            executed = self.executeTaskToBuffer(targetBuffer, thisBatch, schedule)
            if targetBuffer.getTargetTask().getName() != 'End':
                schedule.scheduleBufferToTask(nextTask) # Schedule a new batch into the next task
            return executed


    def executeBufferToTask(self, event, buffer, batch, task, schedule):
        duration = self.plant.taskServesBatch(self, batch, task)
        if duration:
            task.setHoldingBatch(batch)
            if not batch.getBatchCode() in self.executionTime.keys():
                self.executionTime[batch.getBatchCode()] = float(duration)
            else:
                self.executionTime[batch.getBatchCode()] += float(duration)
            return True
        else: 
            return False
    

    def executeTaskToBuffer(self, buffer, batch, schedule):
        sourceTask = buffer.getSourceTask()
        targetTask = buffer.getTargetTask() 

        if buffer.getAvailableCap() >= batch.getNumOfWafers() and batch not in buffer.getHistoryQueueOfBatches():
            sourceTask.batchIsDone() # Removes the batch that the task holds, and sets the Task's state to idle
            self.plant.enqueueBatchIntoBuffer(batch, buffer)
            return True
        else:
            return False
        
    


