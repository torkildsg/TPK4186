"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """
from Batch import Batch
from Buffer import Buffer
from Task import Task
from Machine import Machine
from Plant import Plant
from Printer import Printer
from Event import Event
from Schedule import Schedule
from Simulator import Simulator

import math

class Optimizer:
    def __init__(self, optimizerName):
        self.optimizerName = optimizerName
    
    def generateBatches(self, batchSize, totalNumOfWafers, plant): #All batches will have the same size except for the last one. 
        numBatches = math.ceil(totalNumOfWafers/batchSize)
        lastBatchSize = totalNumOfWafers % batchSize
        for i in range(1,numBatches+1):
            if i == numBatches:
                plant.newBatch(i, lastBatchSize)
            else: plant.newBatch(i,batchSize)
        return plant.getBatches()



