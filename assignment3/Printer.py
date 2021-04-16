"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

import sys
from Batch import Batch
from Buffer import Buffer
from Task import Task
from Plant import Plant
from Event import Event
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Printer:

    def exportPlant(self, plant, filename):
        try:
            file = open(filename, 'w')
        except:
            sys.stderr.write('Cannot open the file {0:s}\n'.format(filename))
            sys.stderr.flush()
            sys.exit()
        self.printPlant(plant, file)
    
    def printPlant(self, plant, file):
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

    def printTask(self, task, file):
        file.write('{0:10}'.format('task\t'))
        file.write('{0:10}\t'.format(task.getName()))
        file.write('\n')
        
    def printEvent(self, event, file):
        file.write('Event {type} at date {date}: '.format(type = event.getNumber(), date = event.getDate()))
        if event.getType() == Event.BUFFER_TO_TASK:
            file.write('Batch {batch} enters {task}.'.format(batch = event.getBatch().getBatchCode(), task = event.getTask().getName()))
        elif event.getType() == Event.TASK_TO_BUFFER:
            file.write('Batch {batch} enters buffer {sourceTask} -> {targetTask}.'.format(batch = event.getBatch().getBatchCode(), sourceTask = event.getBuffer().getSourceTask().getName(), targetTask = event.getBuffer().getTargetTask().getName()))
        file.write('\n')
    
    def printExecution(self, simulator, file):
        file.write("Execution:\n")
        for event in simulator.getExecution():
            self.printEvent(event, file)
    
    def plotTerminationDates(self, terminationDates):
        minDate = np.amin(terminationDates)
        maxDate = np.max(terminationDates)

        n, bins, patches = plt.hist(terminationDates, rwidth=0.7, density = 50, facecolor = 'darkseagreen')
        plt.title('Histogram of termination dates')
        plt.xlabel('Termination date')
        plt.ylabel('Percentage of all terminations')
        file = plt.savefig('terminationDateHistogram.pdf')
        return file

    def printHTML(self, terminationDates, bestTermination):
        self.plotTerminationDates(terminationDates)
        stringOne = """<html>
                          <head>
                            <style>
                                table {
                                    font-family: arial, sans-serif;
                                    border-collapse: collapse;
                                    width: 100%;
                                }

                                td, th {
                                    border: 1px solid #dddddd;
                                    text-align: left;
                                    padding: 8px;
                                }

                                tr:nth-child(even) {
                                    background-color: #dddddd;
                                }
                            </style>
                            <embed src='terminationDateHistogram.pdf' width="800px" height="500px" />
                        </head>
                        <body>"""

        stringTwo = """
            <h2>Table of optimal terminations</h2>
                <table>
                    <tr>
                        <th>Machine-policy combination</th>
                        <th>Machine 1 priority</th>
                        <th>Machine 2 priority</th>
                        <th>Machine 3 priority</th>
                        <th>Date</th> 
                        <th>Size of batch [wafers] </th> 
                        <th>Total duration [seconds] </th> 
                    </tr>"""

        with open('optimized.html', 'w') as file:
            file.write(stringOne)
            file.write('<h2>Table of date-statistics for all terminations</h2>')
            file.write('<table><tr>')
            file.write('<th> Minimum </th>')
            file.write('<th> Maximum </th>')
            file.write('<th> Median </th>')
            file.write('<th> Mean </th>')
            file.write('<th> Standard deviation </th>')
            file.write('</tr>')
            file.write('<tr>')
            file.write('<td>' + str(np.amin(terminationDates)) + '</td>')
            file.write('<td>' + str(np.amax(terminationDates)) + '</td>')
            file.write('<td>' + str(np.median(terminationDates)) + '</td>')
            file.write('<td>' + str(round(np.mean(terminationDates), 2)) + '</td>')
            file.write('<td>' + str(round(np.std(terminationDates), 2)) + '</td>')
            file.write('</tr></table>')
            file.write(stringTwo)
            j = 1
            for i in range(len(bestTermination[0])):
                file.write('<tr>')
                file.write('<td>' + str(j) + '</td>')
                file.write('<td>')
                for k in bestTermination[0][i][0]:
                    file.write(str(k.getName() + ", "))
                file.write('</td><td>')
                for l in bestTermination[0][i][1]:
                    file.write(str(l.getName() + ", "))
                file.write('</td><td>')
                for m in bestTermination[0][i][2]:
                    file.write(str(m.getName() + ", "))
                file.write('</td>')
                file.write('<td>' +  str(bestTermination[2]) +  '</td>')
                file.write('<td>' +  str(bestTermination[1][i]) +  '</td>')
                file.write('<td>' +  str(bestTermination[3][i]) +  '</td>')
                file.write('</tr>')
                j+=1
            file.write('</table>')
            file.write('</body>')
            file.write('</html>')
            file.close()


