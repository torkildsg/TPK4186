"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Batch import Batch
from Buffer import Buffer

class Task:
    TASK = 0
    EVENT = 1
    PROCESSING_BATCH = 2
    IDLE = 3

    def __init__(self, type, name, processTime): # , inputBuffer, outputBuffer, loadTime, unloadTime, processTime
        self.name = name
        self.type = type
        self.state = Task.IDLE
        self.incomingBuffer = []
        self.outgoingBuffer = []
        self.holdingBatch = None
        self.loadTime = 2 # Per buffer going into the task
        self.unloadTime = 2 # Per buffer going into the task
        self.processTime = processTime # Per wafer in a batch
    
    def resetTask(self):
        self.state = Task.IDLE
        self.holdingBatch = None

    def setHoldingBatch(self, batch):
        self.holdingBatch = batch
        self.setState(Task.PROCESSING_BATCH)
        
    def batchIsDone(self):
        self.holdingBatch = None
        self.setState(Task.IDLE)
    
    def getHoldingBatch(self):
        return self.holdingBatch

    def getState(self):
        return self.state
    
    def setState(self, state):
        self.state = state
        
    def getType(self):
        return self.type

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
	
    def getLoadTime(self): # Per batch
        return self.loadTime
	
    def setLoadTime(self, loadTime): # Per batch
        self.loadTime = loadTime
	
    def getUnloadTime(self): # Per batch
        return self.unloadTime
	
    def setUnloadTime(self, unloadTime): # Per batch
        self.unloadTime = unloadTime

    def getProcessTime(self): # Per wafer
        return self.processTime
	
    def setProcessTime(self, processTime): # Per wafer
        self.processTime = processTime

    def addIncomingBuffer(self, buffer):
        self.incomingBuffer.append(buffer)
    
    def getIncomingBuffer(self):
        return self.incomingBuffer

    def addOutgoingBuffer(self, buffer):
        self.outgoingBuffer.append(buffer)

    def getOutgoingBuffer(self):
        return self.outgoingBuffer
    
    def getFirstOfOutgoingBuffers(self):
        return self.outgoingBuffer[0]

    def getFirstOfIncomingBuffers(self):
        return self.incomingBuffer[0]
    
    def taskCanBePerformed(self):
        inputBuffer = self.getFirstOfIncomingBuffers()
        outputBuffer = self.getFirstOfOutgoingBuffers()
        if inputBuffer.isEmpty():
            return False
        else:
            batch = inputBuffer.getFirstBatchInQueue()
            if self.getState() == Task.IDLE and not inputBuffer.isEmpty() and outputBuffer.hasSpace(batch):
                return True
            else: return False
    
