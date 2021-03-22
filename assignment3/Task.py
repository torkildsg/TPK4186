"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

class Task:

    def __init__(self, machine, inputBuffer, outputBuffer, perBatchLoad, unloadTime, perWaferProcessTime):
        self.machine = machine
        self.inputBuffer = inputBuffer
        self.outputBuffer = outputBuffer
        self.perBatchLoad = perBatchLoad
        self.unloadTime = unloadTime
        self.perWaferProcessTime = perWaferProcessTime

        
