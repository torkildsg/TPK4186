"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

class Batch: 

    def __init__(self, batchCode, numOfWafers):
        self.batchCode = batchCode
        self.numOfWafers = numOfWafers # Batch contains 20-50 wafers reguarly 
    
    def getBatchCode(self):
        return self.batchCode
    
    def setNumOfWafers(self, num):
        self.numOfWafers = num
    
    def getNumOfWafers(self):
        return self.numOfWafers
    

