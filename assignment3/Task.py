"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Batch import Batch

class Task:
    TASK = 0
    EVENT = 1
    PROCESSING_BUFFER = 2
    IDLE = 3

    def __init__(self, type, name): # , inputBuffer, outputBuffer, loadTime, unloadTime, processTime
        self.name = name
        self.type = type
        self.state = Task.IDLE
        self.incomingBuffer = []
        self.outgoingBuffer = []
        self.loadTime = 2 # Per buffer going into the task
        self.unloadTime = 2 # Per buffer going into the task
        self.processTime = 0 # Per wafer in a batch
        self.duration = float(self.getUnloadTime() + self.getLoadTime() + self.getProcessTime())
        """self.earlyStartDate = -1
        self.earlyCompletionDate = -1
        self.lateStartDate = -1
        self.lateCompletionDate = -1"""

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
    
    """def getEarlyStartDate(self):
        return self.earlyStartDate
    
    def setEarlyStartDate(self, date):
        self.earlyStartDate = date

    def getEarlyCompletionDate(self):
        return self.earlyCompletionDate
    
    def setEarlyCompletionDate(self, date):
        self.earlyCompletionDate = date

    def getLateStartDate(self):
        return self.lateStartDate
    
    def setLateStartDate(self, date):
        self.lateStartDate = date

    def getLateCompletionDate(self):
        return self.lateCompletionDate
    
    def setLateCompletionDate(self, date):
        self.lateCompletionDate = date"""

    

    
	

