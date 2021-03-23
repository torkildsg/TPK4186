"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Buffer import Buffer
from Task import Task

class Machine:

    def __init__(self, machineName):
        self.machineName = machineName
        self.tasks = dict()
    
    def getName(self):
        return self.machineName

    def lookForTask(self, name):
        return self.tasks.get(name, False)
    
    def newTask(self, name):
        if lookForTask(name):
            return False
        else:
            task = Task(name)
            self.tasks[name] = task
    
    def deleteTask(self, task):
        del self.tasks[task.getName()]
    
Machine = Machine("enigma")
