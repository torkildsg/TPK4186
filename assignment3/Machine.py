"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Buffer import Buffer
from Task import Task

class Machine:

    def __init__(self, machineName):
        self.machineName = machineName
        self.tasks = dict()
    
    def getName(self):
        return self.machineName
    
    def getTasks(self):
        return self.tasks

    def lookForTask(self, name):
        return self.tasks.get(name, None)
    
    

