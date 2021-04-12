""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

class Event:
    BATCH_TO_TASK = 1
    BATCH_TO_BUFFER = 2

    def __init__(self, type, number, date):
        self.type = type
        self.number = number
        self.date = date
        self.batch = None
        self.buffer = None
        self.task = None
    
    def getType(self):
        return self.type
    
    def setType(self, type):
        self.type = type
    
    def getDate(self):
        return self.date
    
    def getNumber(self):
        return self.number
    
    def setBatch(self, batch):
        self.batch = batch
    
    def getBatch(self):
        return self.batch
    
    def setBuffer(self, buffer):
        self.buffer = buffer
    
    def getBuffer(self):
        return self.buffer
    
    def setTask(self, task):
        self.task = task
    
    def getTask(self):
        return self.task