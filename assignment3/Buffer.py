"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

class Buffer:

    def __init__(self, capacity, queueOfBatches):
        self.capacity = capacity
        self.queueOfBatches = queueOfBatches # FIFO-queue: Only use .pop(0) to get, and .append() to add
    
    def enqueueBuffer(self, batch):
        if len(self.queueOfBatches) == capacity:
            return None
        else:
            self.queueOfBatches.append(batch)

    def dequeueBuffer(self):
        if len(self.queueOfBatches) < 1:
            return None
        return self.queue.pop(0)

