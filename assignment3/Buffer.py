""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

class Buffer:

    def __init__(self, sourceTask, targetTask):
        self.capacity = 120 # Defined from the assignment 
        self.wafers = 0
        self.queueOfBatches = [] # FIFO-queue
        self.historyQueueOfBatches = []
        self.sourceTask = sourceTask
        self.targetTask = targetTask

    def resetBuffer(self):
        self.historyQueueOfBatches = []
        self.wafers = 0
        self.queueOfBatches = []
    
    def isEmpty(self):
        return self.queueOfBatches == []
    
    def getHistoryQueueOfBatches(self):
        return self.historyQueueOfBatches

    def appendToHistoryQueueOfBatches(self, batch):
        self.historyQueueOfBatches.append(batch)

    def hasSpace(self, batch):
        if (self.getAvailableCap() - batch.getNumOfWafers()) > 0:
            return True
        else: return False

    def getAvailableCap(self):
        return (self.capacity - self.getWafers())
    
    def setWafers(self):
        count = 0
        for batch in self.queueOfBatches:
            count += batch.getNumOfWafers()
        self.wafers = count
        
    def getWafers(self):
        self.setWafers()
        return self.wafers
    
    def getCapacity(self):
        return self.capacity
    
    def setCapacity(self, cap):
        self.capacity = cap
    
    def getCapacity(self):
        return self.capacity

    def setTargetTask(self, task):
        self.targetTask = task
    
    def getTargetTask(self):
        return self.targetTask
    
    def setSourceTask(self, task):
        self.sourceTask = task
    
    def getSourceTask(self):
        return self.sourceTask

    def getQueueOfBatches(self):
        return self.queueOfBatches

    def getFirstBatchInQueue(self):
        if len(self.queueOfBatches) > 0:
            return self.queueOfBatches[0]
        else: return False
    
    def getLastBatchInQueue(self):
        return self.queueOfBatches[-1]
    
    def enqueueBuffer(self, batch):
        if not self.hasSpace(batch):
            return False
        else:
            self.queueOfBatches.append(batch)
            self.appendToHistoryQueueOfBatches(batch)
            self.setWafers()

    def dequeueBuffer(self):
        if len(self.queueOfBatches) < 1:
            return None
        popped = self.queueOfBatches.pop(0)
        self.setWafers()
        return popped

