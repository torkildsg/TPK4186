"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

class Batch: 

    IN_BUFFER = 0
    PROCESSING_TASK = 1

    def __init__(self, batchCode, numOfWafers):

        """ From the task we have: 
        Note that it is required that all batches have the same size. """
        
        self.batchCode = batchCode
        self.numOfWafers = numOfWafers # Batch contains 20-50 wafers reguarly 
        self.state = Batch.IN_BUFFER
    
    def getBatchCode(self):
        return self.batchCode
    
    def setNumOfWafers(self, num):
        self.numOfWafers = num
    
    def getNumOfWafers(self):
        return self.numOfWafers

    def getState(self):
        return self.state
    
    def setState(self, state):
        self.state = state
    

