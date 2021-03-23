"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

class Batch: 

    def __init__(self, bufferCode, numOfWafers):
        self.bufferCode = bufferCode
        self.numOfWafers = numOfWafers # Batch contains 20-50 wafers reguarly 
    
    def getBufferCode(self):
        return self.bufferCode
    
    def setNumOfWafers(self, num):
        self.numOfWafers = num
    
    def getNumOfWafers(self):
        return self.numOfWafers
    

