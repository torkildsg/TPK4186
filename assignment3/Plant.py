"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Batch import Batch
from Buffer import Buffer
from Task import Task
from Machine import Machine

class Plant:

    def __init__(self, name):
        self.name = name
        self.machines = []
        self.allBuffers = []

    def getName(self):
        return self.name
    
    def getMachines(self):
        return self.machines
    
    def getAllBuffers(self):
        return self.allBuffers

    def newMachine(self, name):
        machine = Machine(name)
        self.machines.append(machine)
    
    def deleteMachine(self, machine):
        for i in self.machines:
            if i == machine:
                self.machines.remove(machine)
    
    def newBuffer(self, capacity, sourceTask, targetTask):
        buffer = Buffer(capacity, sourceTask, targetTask)
        self.allBuffers.append(buffer)
        sourceTask.addOutgoingConstraint(buffer)
        targetTask.addIncomingConstraint(buffer)
    
    def deleteBuffer(self, sourceTask, targetTask):
        for buffer in self.allBuffers:
            if buffer.getSourceTask() == sourceTask and buffer.getTargetTask() == targetTask:
                self.allBuffers.remove(buffer)
