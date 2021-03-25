"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

class Buffer:

    def __init__(self, sourceTask, targetTask):
        self.capacity = 120 # 120?
        self.queueOfBatches = [] # FIFO-queue: Only use .pop(0) to get, and .append() to add
        self.sourceTask = sourceTask
        self.targetTask = targetTask

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

    def getQueue(self):
        return self.queueOfBatches
    
    def enqueueBuffer(self, batch):
        count = 0
        for batch in self.queueOfBatches:
            count += batch
        if count >= capacity:
            return None
        else:
            self.queueOfBatches.append(batch)

    def dequeueBuffer(self):
        if len(self.queueOfBatches) < 1:
            return None
        return self.queueOfBatches.pop(0)

