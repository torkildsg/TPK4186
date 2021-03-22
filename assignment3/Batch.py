"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

class Batch:

    def __init__(self, bufferCode, numOfWafers):
        self.bufferCode = bufferCode
        self.numOfWafers = numOfWafers
    
    def getBufferCode(self):
        return self.bufferCode
    
    def setNumOfWafers(self, num):
        self.numOfWafers = num
    
    def getNumOfWafers(self):
        return self.numOfWafers
    
    
