"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

class Task:

    def __init__(self, name): # , inputBuffer, outputBuffer, loadTime, unloadTime, processTime
        self.name = name
        self.inputBuffer = inputBuffer
        self.outputBuffer = outputBuffer
        self.loadTime = loadTime # Per buffer going into the task
        self.unloadTime = unloadTime # Per buffer going into the task
        self.processTime = processTime # Per wafer in a batch
        self.incomingConstraints = []
        self.outgoingConstraints = []   

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getInputBuffer(self):
        return self.inputBuffer
	
    def setInputBuffer(self, input):
        self.inputBuffer = input

    def getOutputBuffer(self):
        return self.outputBuffer

    def setOutputBuffer(self, outputBuffer):
        self.outputBuffer = outputBuffer
	
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

    def addIncomingConstraints(self, constraint):
        self.incomingConstraints.append(constraint)

    def getIncomingContraints(self):
        return self.incomingConstraints

    def addOutgoingConstrains(self, contraint):
        self.outgoingConstraints.append(contraint)

    def getOutgoingConstraints(self):
        return self.outgoingConstraints 
	

