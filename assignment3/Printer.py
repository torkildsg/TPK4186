"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

import sys
from Batch import Batch
from Buffer import Buffer
from Task import Task
from Machine import Machine

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
        file.write('plant\t{0:10}\n\n'.format(plant.getName()))
        for task in plant.getAllTasksEvents():
            self.printTaskCSV(task, file)
        
    def printTaskCSV(self, task, file):
        if task.getType() == Task.TASK:
            file.write('{0:10}'.format('task\t'))
        else:
            file.write('{0:11}'.format('event\t'))
        file.write('{0:10}\t'.format(task.getName()))
        first = True

        """for buffer in task.getIncomingBuffers():
            otherTask = buffer.getSourceTask()
            if first:
                first = False
            else:
                file.write(' ')
            file.write('{0:s}'.format(otherTask.getName()))"""
        #file.write('\t')
        first = True
        for buffer in task.getOutgoingBuffers():
            otherTask = buffer.getTargetTask()
            if first:
                first = False
            else:
                file.write(' ')
            file.write('{0:10}'.format(otherTask.getName()))
        file.write("{0:d}\t".format(task.getDuration()))
        file.write('\n')
        

