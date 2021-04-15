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
    
    def initiateWaferProductionPlant(self, batchSize, totalNumOfWafers):
        # initiate a new plant
        waferproduction = Plant("Waferproduction") 
        
        # initiate the three machines
        machine1 = waferproduction.newMachine("Machine 1") 
        machine2 = waferproduction.newMachine("Machine 2")
        machine3 = waferproduction.newMachine("Machine 3")
        
        # Initiate the tasks
        start = waferproduction.newEvent("Start")
        task1 = waferproduction.newTask("Task 1", 0.5, machine1)
        task2 = waferproduction.newTask("Task 2", 3.5, machine2)
        task3 = waferproduction.newTask("Task 3", 1.2, machine1)
        task4 = waferproduction.newTask("Task 4", 3, machine3)
        task5 = waferproduction.newTask("Task 5", 0.8, machine2)
        task6 = waferproduction.newTask("Task 6", 0.5, machine1)
        task7 = waferproduction.newTask("Task 7", 1, machine2)
        task8 = waferproduction.newTask("Task 8", 1.9, machine3)
        task9 = waferproduction.newTask("Task 9", 0.3, machine1)
        end = waferproduction.newEvent("End")

        # Generate the batches and add them to the plant
        newBatches = self.generateBatches(batchSize, totalNumOfWafers, waferproduction)

        return waferproduction
        

