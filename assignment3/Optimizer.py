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
from itertools import permutations
import itertools
class Optimizer:
    
    def __init__(self, optimizerName):
        self.optimizerName = optimizerName
        self.allPossiblePolicycombinations = []
    
    def generateBatches(self, batchSize, totalNumOfWafers, plant): #All batches will have the same size except for the last one. 
        numBatches = math.ceil(totalNumOfWafers/batchSize)
        lastBatchSize = totalNumOfWafers % batchSize
        for i in range(1,numBatches+1):
            if i == numBatches:
                plant.newBatch(i, lastBatchSize)
            else: plant.newBatch(i,batchSize)
        return plant.getBatches()

    def generateOperationPoliciesForMachines(self, plant):
        machinesInPlant = plant.getAllMachines()
        for machine in machinesInPlant:
            allMachinePolicies = []
            for policy in permutations(machine.getTasks()):
                allMachinePolicies.append(list(policy))
            machine.setMachinePolicies(allMachinePolicies)

    def generateAllPossiblePolicycombinations(self, plant):
        machinesInPlant = plant.getAllMachines()
        threeDimensionalList = [] #3 Dimensional list: [[M1_PolicyList1, M1_PolicyList2, ..], [M2_PolicyList1, M2_PolicyList2, ..], [M3_PolicyList1, M3_PolicyList2, ..]]
        
        for machine in machinesInPlant:
            listOfThisMachinesPolicyLists = []
            for thisMachinesPolicyLists in machine.getMachinePolicies():
                listOfThisMachinesPolicyLists.append(thisMachinesPolicyLists)
            threeDimensionalList.append(listOfThisMachinesPolicyLists)
        
        allPossiblePolicycombinations = [] # [ [[M1_PolicyList1], [M2_PolicyList1], [M3_PolicyList1]], [[M1_PolicyList2], [M2_PolicyList1], [M3_PolicyList1]], ..]
        for element in itertools.product(*threeDimensionalList):
            allPossiblePolicycombinations.append(list(element))

        self.allPossiblePolicycombinations = allPossiblePolicycombinations


        

