"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Batch import Batch
from Buffer import Buffer
from Task import Task
from Machine import Machine

class Plant:

    def __init__(self, name):
        self.name = name
        self.allMachines = []
        self.allBuffers = []
        self.allTasksEvents = []
        self.batches = []

    def resetPlant(self):
        for buffer in self.allBuffers:
            buffer.resetBuffer()
        for task in self.allTasksEvents:
            task.resetTask()
        for machine in self.allMachines:
            machine.resetMachine()
        self.batches = []
        return True
    
    def getName(self):
        return self.name

    def newBatch(self, batchCode, numOfWafers):
        if numOfWafers > 50 or numOfWafers < 20:
            return False
        else:
            batch = Batch(batchCode, numOfWafers)
            self.batches.append(batch)
            return batch
    
    def deleteBatch(self, batch):
        for b in self.batches:
            if b.getName() == batch.getName():
                self.batches.remove(batch)

    def getBatches(self):
        return self.batches
    
    def newTask(self, name, processtime, machine):
        if machine.lookForTask(name) is not None:
            return False
        else:
            task = Task(Task.TASK, name, processtime)
            machine.tasks[name] = task
            self.allTasksEvents.append(task)
        return task
        
    def deleteTask(self, task, machine):
        del machine.tasks[task.getName()]

    def newEvent(self, name):
        event = Task(Task.EVENT, name, 0)
        self.allTasksEvents.append(event)
        return event

    def getAllTasksEvents(self):
        return self.allTasksEvents
    
    def getFirstTask(self):
        return self.allTasksEvents[1]
    
    def getStartBuffer(self):
        return self.allBuffers[0]
    
    def getEndBuffer(self):
        return self.allBuffers[-1]
    
    def deleteEvent(self, event):
        for e in self.allTasksEvents:
            if e == event:
                self.allTasksEvents.remove(event)

    def newMachine(self, name):
        machine = Machine(name)
        self.allMachines.append(machine)
        return machine
    
    def deleteMachine(self, machine):
        for i in self.allMachines:
            if i == machine:
                self.allMachines.remove(machine)
    
    def getAllMachines(self):
        return self.allMachines

    def getMachine(self, task):
        for machine in self.getAllMachines():
            for t in machine.getTasks():
                if t == task:
                    return machine
                else: continue
    
    def newBuffer(self, sourceTask, targetTask):
        buffer = Buffer(sourceTask, targetTask)
        self.allBuffers.append(buffer)
        sourceTask.addOutgoingBuffer(buffer)
        targetTask.addIncomingBuffer(buffer)
        return buffer
    
    def deleteBuffer(self, sourceTask, targetTask):
        for buffer in self.allBuffers:
            if buffer.getSourceTask() == sourceTask and buffer.getTargetTask() == targetTask:
                self.allBuffers.remove(buffer)

    def getAllBuffers(self):
        return self.allBuffers

    def batchEntersTask(self, batch):
        batch.setState(Batch.PROCESSING_TASK)
    
    def batchEntersBuffer(self, batch):
        batch.setState(Batch.IN_BUFFER)

    def enqueueBatchIntoBuffer(self, batch, buffer):
        if batch in buffer.getQueueOfBatches():
            return False
        else:
            self.batchEntersBuffer(batch)
            buffer.enqueueBuffer(batch)
            return True
    
    def dequeueBatchFromBuffer(self, batch):
        for buffer in self.allBuffers:
            for j in buffer.getQueueOfBatches():
                if j == batch:
                    buffer.dequeueBuffer()
                    return True
                else: continue
        return False
    
    def isMachineBusy(self, simulator, machine):
        for t in machine.getTasks():    
            if t.getState() == Task.PROCESSING_BATCH: # If this tasks' machine is already processing a batch in a other task, return false
                return True
        return False

    def taskServesBatch(self, simulator, batch, task):
        machine = self.getMachine(task)
        if self.isMachineBusy(simulator, machine):
            return False
        else:
            # Else dequeue the batch from its buffer, and set the task to process the batch.
            if self.dequeueBatchFromBuffer(batch):
                self.batchEntersTask(batch)
                task.setState(Task.PROCESSING_BATCH)
                duration = float(task.getLoadTime() + task.getUnloadTime() + task.getProcessTime() * batch.getNumOfWafers())
                return duration
        
    """ Task 3 """
    def runMachinePolicy(self, simulator, schedule, machine, priority):
        for task in priority:
            if not self.isMachineBusy(simulator, machine) and task.taskCanBePerformed():
                schedule.scheduleBufferToTask(task)
                return True
            else: continue
        return False


        