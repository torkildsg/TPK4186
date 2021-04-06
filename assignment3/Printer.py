"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

import sys
from Batch import Batch
from Buffer import Buffer
from Task import Task
from Machine import Machine
from Calculator import Calculator
from Plant import Plant


class Printer:

    def exportPlantCSV(self, plant, filename):
        try:
            file = open(filename, 'w')
        except:
            sys.stderr.write('Cannot open the file {0:s}\n'.format(filename))
            sys.stderr.flush()
            sys.exit()
        self.printPlantCSV(plant, file)
    
    def printPlantCSV(self, plant, file):
        file.write('{text}        {number}\n'.format(text = 'Name of plant:', number = plant.getName()))
        file.write('{text}   {number}\n'.format(text = 'Number of machines:', number = len(plant.getAllMachines())))
        file.write('{text}      {number}\n'.format(text = 'Number of tasks:', number = len(plant.getAllTasksEvents())-2))
        file.write('{text}    {number}\n\n'.format(text = 'Number of buffers:', number = len(plant.getAllBuffers())))

        file.write('Batch states:\n')
        file.write('Batch in buffer = 0\n')
        file.write('Batch is processed by task = 1\n\n')

        for batch in plant.getBatches():
            file.write('{text}{number}'.format(text = 'Batchcode:', number = batch.getBatchCode()))
            file.write('{text}{number}'.format(text = '\t  State of batch:', number = batch.getState()))
            file.write('{text}{number}'.format(text = '\t  Number of wafers:', number = batch.getNumOfWafers()))
            file.write('\n')
        
        file.write('\n')

        for buffer in plant.getAllBuffers():
            file.write('Buffer: {sourcetask} --> {targettask}'.format(sourcetask = buffer.getSourceTask().getName(), targettask = buffer.getTargetTask().getName()))
            if buffer.getTargetTask().getName() == 'End':
                file.write('   \tCapacity: {num}/{cap}\n'.format(num = buffer.getWafers(), cap = buffer.getCapacity()))
            else:
                file.write('  \tCapacity: {num}/{cap}\n'.format(num = buffer.getWafers(), cap = buffer.getCapacity()))

    def printTaskCSV(self, task, file):
        """if task.getType() == Task.TASK:
            file.write('{0:10}'.format('task\t'))
        else:
            file.write('{0:11}'.format('event\t'))
        file.write('{0:10}\t'.format(task.getName()))

        first = True
        for buffer in task.getOutgoingBuffers():
            targetTask = buffer.getTargetTask()
            if first:
                first = False
            else:
                file.write(' ')
            file.write('{0:10}'.format(targetTask.getName()))
        
        if task.getName() == 'End':
            file.write('{0:10}'.format("    "))
        """

        file.write('{0:10}'.format('task\t'))
        file.write('{0:10}\t'.format(task.getName()))


        """ Uncertain if we need this
        file.write("{0:d}\t".format(task.getDuration()))
        file.write('\t{0:g}'.format(task.getEarlyStartDate()))
        file.write('\t{0:g}'.format(task.getEarlyCompletionDate()))
        file.write('\t{0:g}'.format(task.getLateStartDate()))
        file.write('\t{0:g}'.format(task.getLateCompletionDate()))"""

        file.write('\n')
    
    def printSchedule(self, simulator, file):
        file.write('Schedule:\n')
        for event in simulator.getSchedule():
            self.printEvent(event, file)
        
    def printEvent(self, event, file):
        file.write('\t{type}\t{date}'.format(type = event.getType(), date = event.getDate()))
        
        