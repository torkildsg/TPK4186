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

    def newEvent(self, name):
        event = Task(name)
        return event

    def getName(self):
        return self.name
    
    def getMachines(self):
        return self.machines
    
    def getAllBuffers(self):
        return self.allBuffers

    def newMachine(self, name):
        machine = Machine(name)
        self.machines.append(machine)
        return machine
    
    def deleteMachine(self, machine):
        for i in self.machines:
            if i == machine:
                self.machines.remove(machine)
    
    def newBuffer(self, sourceTask, targetTask):
        buffer = Buffer(sourceTask, targetTask)
        self.allBuffers.append(buffer)
        sourceTask.setOutgoingBuffer(buffer)
        targetTask.setIncomingBuffer(buffer)
        return buffer
    
    def deleteBuffer(self, sourceTask, targetTask):
        for buffer in self.allBuffers:
            if buffer.getSourceTask() == sourceTask and buffer.getTargetTask() == targetTask:
                self.allBuffers.remove(buffer)

""" Testing Task 1 """
waferprod = Plant("Waferprod")

"""batch1 = Batch(1, 20)
batch2 = Batch(2, 25)
batch3 = Batch(3, 30)
batch4 = Batch(4, 35)
batch5 = Batch(5, 40)
batch6 = Batch(6, 45)
batch7 = Batch(7, 50)"""

machine1 = waferprod.newMachine("machine1")
machine2 = waferprod.newMachine("machine2")
machine3 = waferprod.newMachine("machine3")

start = waferprod.newEvent("Start")
task1 = machine1.newTask("Task1")
task3 = machine1.newTask("Task3")
task6 = machine1.newTask("Task6")
task9 = machine1.newTask("Task9")

task2 = machine2.newTask("Task2")
task5 = machine2.newTask("Task5")
task7 = machine2.newTask("Task7")

task4 = machine3.newTask("Task4")
task8 = machine3.newTask("Task8")
end = waferprod.newEvent("End")

waferprod.newBuffer(start, task1)
waferprod.newBuffer(task1, task2)
waferprod.newBuffer(task2, task3)
waferprod.newBuffer(task3, task4)
waferprod.newBuffer(task4, task5)
waferprod.newBuffer(task5, task6)
waferprod.newBuffer(task6, task7)
waferprod.newBuffer(task8, task9)
waferprod.newBuffer(task9, end)

task1.setProcessTime(0.5)
task2.setProcessTime(3.5)
task3.setProcessTime(1.2)
task4.setProcessTime(3)
task5.setProcessTime(0.8)
task6.setProcessTime(0.5)
task7.setProcessTime(1)
task8.setProcessTime(1.9)
task9.setProcessTime(0.3)

print(waferprod.name)
print(len(waferprod.allBuffers))
for m in waferprod.machines:
    print(m.getName())





