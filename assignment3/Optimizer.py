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
        self.allPossiblePolicyCombinations = []
    
    def generateBatches(self, batchSize, totalNumOfWafers, plant):  
        numBatches = math.ceil(totalNumOfWafers/batchSize) # If totalNumOfWafers % batchSize > 0, we produce an extra batch to ensure that enough wafers is produced. 
        for i in range(1, numBatches+1):                    # In this case, the number of wafers produced will be greater than totalNumOfWafers. 
            plant.newBatch(i,batchSize)                       # This a necessity, since all batches have to be the same size (we assume).
        return plant.getBatches()
    
    def initiatePlant(self, plant, batchSize, totalNumOfWafers):
        allBatches = self.generateBatches(batchSize, totalNumOfWafers, plant)
        if allBatches:
            for batch in allBatches:
                plant.enqueueBatchIntoBuffer(batch, plant.getStartBuffer())
            return True
        else: return False

    def generateOperationPoliciesForMachines(self, plant):
        machinesInPlant = plant.getAllMachines()
        for machine in machinesInPlant:
            allMachinePolicies = []
            for policy in permutations(machine.getTasks()):
                allMachinePolicies.append(list(policy))
            machine.setMachinePolicies(allMachinePolicies)

    def generateAllPossiblePolicyCombinations(self, plant):
        self.generateOperationPoliciesForMachines(plant)
        machinesInPlant = plant.getAllMachines()
        threeDimensionalList = [] #3 Dimensional list: [[M1_PolicyList1, M1_PolicyList2, ..], [M2_PolicyList1, M2_PolicyList2, ..], [M3_PolicyList1, M3_PolicyList2, ..]]
        
        for machine in machinesInPlant:
            listOfThisMachinesPolicyLists = []
            for thisMachinesPolicyLists in machine.getMachinePolicies():
                listOfThisMachinesPolicyLists.append(thisMachinesPolicyLists)
            threeDimensionalList.append(listOfThisMachinesPolicyLists)
        
        allPossiblePolicyCombinations = [] # [ [[M1_PolicyList1], [M2_PolicyList1], [M3_PolicyList1]], [[M1_PolicyList2], [M2_PolicyList1], [M3_PolicyList1]], ..]
        for element in itertools.product(*threeDimensionalList):
            allPossiblePolicyCombinations.append(list(element))

        self.allPossiblePolicyCombinations = allPossiblePolicyCombinations


        

