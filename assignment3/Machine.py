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
    
    def newTask(self, name):
        if self.lookForTask(name) is not None:
            return False
        else:
            task = Task(name)
            self.tasks[name] = task
        return task
    
    def deleteTask(self, task):
        del self.tasks[task.getName()]
    

