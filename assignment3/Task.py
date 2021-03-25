"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Batch import Batch

class Task:
    TASK = 0
    EVENT = 1

    def __init__(self, type, name): # , inputBuffer, outputBuffer, loadTime, unloadTime, processTime
        self.name = name
        self.type = type
        self.incomingBuffer = []
        self.outgoingBuffer = []
        self.loadTime = 2 # Per buffer going into the task
        self.unloadTime = 2 # Per buffer going into the task
        self.processTime = 0 # Per wafer in a batch
        self.duration = 0
        
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
    
    def setDuration(self, batch):
        self.duration = float(self.getUnloadTime() + self.getLoadTime() + self.getProcessTime() * batch.getNumOfWafers())
    
    def getDuration(self):
        return self.duration

    def addIncomingBuffer(self, buffer):
        self.incomingBuffer.append(buffer)

    def getIncomingBuffers(self):
        return self.incomingBuffer

    def addOutgoingBuffer(self, buffer):
        self.outgoingBuffer.append(buffer)

    def getOutgoingBuffers(self):
        return self.outgoingBuffer
	

