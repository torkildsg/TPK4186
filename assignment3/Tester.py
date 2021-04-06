"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Batch import Batch
from Buffer import Buffer
from Task import Task
from Machine import Machine
from Calculator import Calculator
from Plant import Plant
from Printer import Printer

""" Testing Task 1 """
waferprod = Plant("Waferprod")

batch1 = waferprod.newBatch(1, 20)
batch2 = waferprod.newBatch(2, 25)
batch3 = waferprod.newBatch(3, 30)
batch4 = waferprod.newBatch(4, 35)
batch5 = waferprod.newBatch(5, 40)
batch6 = waferprod.newBatch(6, 45)
batch7 = waferprod.newBatch(7, 50)

machine1 = waferprod.newMachine("machine1")
machine2 = waferprod.newMachine("machine2")
machine3 = waferprod.newMachine("machine3")

start = waferprod.newEvent("Start")
task1 = waferprod.newTask("Task1", 0.5, machine1)
task3 = waferprod.newTask("Task3", 1.2, machine1)
task6 = waferprod.newTask("Task6", 0.5, machine1)
task9 = waferprod.newTask("Task9", 0.3, machine1)

task2 = waferprod.newTask("Task2", 3.5, machine2)
task5 = waferprod.newTask("Task5", 0.8, machine2)
task7 = waferprod.newTask("Task7", 1, machine2)

task4 = waferprod.newTask("Task4", 3, machine3)
task8 = waferprod.newTask("Task8", 1.9, machine3)
end = waferprod.newEvent("End")

startbuffer = waferprod.newBuffer(start, task1)
buffer1 = waferprod.newBuffer(task1, task2)
buffer2 = waferprod.newBuffer(task2, task3)
buffer3 = waferprod.newBuffer(task3, task4)
buffer4 = waferprod.newBuffer(task4, task5)
buffer5 = waferprod.newBuffer(task5, task6)
buffer6 = waferprod.newBuffer(task6, task7)
buffer7 = waferprod.newBuffer(task7, task8)
buffer8 = waferprod.newBuffer(task8, task9)
endbuffer = waferprod.newBuffer(task9, end)

"""print(waferprod.name)
for buffer in waferprod.allBuffers:
    print(buffer)
for m in waferprod.machines:
    print(m.getName())

for task in waferprod.getAllTasksEvents():
    print(task.getName())"""

#calc = Calculator()
#calc.calculateDates(waferprod)

waferprod.enqueueBatchIntoBuffer(batch1, startbuffer)
waferprod.enqueueBatchIntoBuffer(batch2, startbuffer)
waferprod.enqueueBatchIntoBuffer(batch3, startbuffer)
waferprod.enqueueBatchIntoBuffer(batch4, startbuffer)
waferprod.enqueueBatchIntoBuffer(batch5, startbuffer)

printer = Printer()
printer.exportPlantCSV(waferprod, 'plant.csv')

waferprod.batchEntersTask(batch1, task1)
