"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Schedule import Schedule
from Plant import Plant
from Event import Event
from Task import Task
from Buffer import Buffer
import math

class Simulator:
    def __init__(self, plant):
        self.plant = plant
        self.execution = [] # The executed schedule
        self.eventNumber = 0
        self.terminationDates = [] # All termnation dates
        self.bestTermination = [[], [], math.inf] # [[optimal policyCombinations], [optimal batchsizes], the best date] 

    def resetSimulator(self):
        self.execution = []
        self.eventNumber = 0
        return True

    def getExecution(self):
        return self.execution
    
    def simulationLoop(self, schedule):
        self.execution = []
        firstTask = schedule.getPlant().getFirstTask() 
        schedule.scheduleBufferToTask(firstTask)

        while not schedule.isCurrentScheduleEmpty(): 
            event = schedule.popFirstEvent()
            if self.executeEvent(event, schedule):
                self.execution.append(event)
            else: continue
    
    def executeEvent(self, event, schedule):
        schedule.currentDate = event.getDate()
        thisBatch = event.getBatch()

        if event.getType() == Event.BUFFER_TO_TASK:
            targetTask = event.getTask()
            thisBuffer = event.getBuffer()
            sourceTask = thisBuffer.getSourceTask()
            nextBuffer = targetTask.getFirstOfOutgoingBuffers()
            task = thisBuffer.getTargetTask()

            if not thisBuffer.isEmpty() and sourceTask.getName() != 'End':
                executed = self.executeBufferToTask(event, thisBuffer, thisBatch, targetTask, schedule)

                #if nextBuffer.hasSpace(thisBatch):
                schedule.scheduleTaskToBuffer(nextBuffer)  # Schedule the batch into the outputbuffer
                if len(thisBuffer.getQueueOfBatches()) > 0:
                    schedule.scheduleBufferToTask(thisBuffer.getTargetTask())
                return executed 

        elif event.getType() == Event.TASK_TO_BUFFER:
            thisTask = event.getTask()
            targetBuffer = thisTask.getFirstOfOutgoingBuffers()
            sourceBuffer = thisTask.getFirstOfIncomingBuffers()
            nextTask = targetBuffer.getTargetTask()
            #if targetBuffer.hasSpace(thisBatch):
            executed = self.executeTaskToBuffer(targetBuffer, thisBatch, schedule)
            if targetBuffer.getTargetTask().getName() != 'End' and len(targetBuffer.getQueueOfBatches()) > 0:
                schedule.scheduleBufferToTask(nextTask) # Schedule a new batch into the next task
            return executed
            #else: return False

    def executeBufferToTask(self, event, buffer, batch, task, schedule):
        duration = self.plant.taskServesBatch(self, batch, task)
        if duration:
            task.setHoldingBatch(batch)
            return True
        else: return False
    
    def executeTaskToBuffer(self, buffer, batch, schedule):
        sourceTask = buffer.getSourceTask()
        if (buffer.getAvailableCap() >= batch.getNumOfWafers()) and (batch not in buffer.getHistoryQueueOfBatches()):
            sourceTask.batchIsDone() # Removes the batch that the task holds, and sets the Task's state to idle
            self.plant.enqueueBatchIntoBuffer(batch, buffer)
            return True
        else: return False
        

    """ Task 3 """

    def simulationLoopForOptimizer(self, schedule, policyCombination):
        self.execution = []
        schedule.currentSchedule = []
        plant = schedule.getPlant()
        firstTask = plant.getFirstTask() 
        schedule.scheduleBufferToTask(firstTask)
        lastBatch = plant.getStartBuffer().getLastBatchInQueue()
        endBuffer = plant.getEndBuffer().getQueueOfBatches()

        while lastBatch not in endBuffer and not schedule.isCurrentScheduleEmpty():
            event = schedule.popFirstEvent()
            if self.executeEventForOptimizer(event, schedule): #Her brukte vi før eecuteEventForOptimizer
                self.execution.append(event)
                for index, machine in enumerate(plant.getAllMachines(), 0):
                    plant.runMachinePolicy(self, schedule, machine, policyCombination[index])
            else: 
                continue
    
    def executeEventForOptimizer(self, event, schedule):
        schedule.currentDate = event.getDate()
        thisBatch = event.getBatch()

        if event.getType() == Event.BUFFER_TO_TASK:
            targetTask = event.getTask()
            thisBuffer = event.getBuffer()
            sourceTask = thisBuffer.getSourceTask()
            nextBuffer = targetTask.getFirstOfOutgoingBuffers()

            if not thisBuffer.isEmpty() and sourceTask.getName() != 'End':
                executed = self.executeBufferToTask(event, thisBuffer, thisBatch, targetTask, schedule)
                if nextBuffer.hasSpace(thisBatch):
                    schedule.scheduleTaskToBuffer(nextBuffer)  # Schedule the batch into the outputbuffer
                return executed

        elif event.getType() == Event.TASK_TO_BUFFER:
            thisTask = event.getTask()
            targetBuffer = thisTask.getFirstOfOutgoingBuffers()
            executed = self.executeTaskToBuffer(targetBuffer, thisBatch, schedule)
            return executed

    def MonteCarloSimulation(self, optimizer, plant, schedule, numOfWafers):
        optimizer.generateAllPossiblePolicyCombinations(plant)
        allPolicyCombinations = optimizer.allPossiblePolicyCombinations
        allPossibleBatchSizes = [i for i in range(20, 51)] # Testing 31 (20-50) different batch-sizes. 
        
        for batchSize in allPossibleBatchSizes:
            for policyComb in allPolicyCombinations:    
                plant.resetPlant()
                schedule.resetSchedule()
                self.resetSimulator()
            
                optimizer.initiatePlant(plant, batchSize, numOfWafers) 
                self.simulationLoopForOptimizer(schedule, policyComb)
                self.terminationDates.append(schedule.currentDate)
                
                if schedule.currentDate < self.bestTermination[2]:
                    self.bestTermination[0].append(policyComb)
                    self.bestTermination[1].append(batchSize)
                    self.bestTermination[2] = schedule.currentDate
                elif schedule.currentDate == self.bestTermination[2]:
                    self.bestTermination[0].append(policyComb)
                    self.bestTermination[1].append(batchSize)
        
        # Returns the list of all terminationdates, and the list of the best terminations that has the lowest date-number. 
        return self.terminationDates, self.bestTermination
        
    


    