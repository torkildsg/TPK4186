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
    
    """ Denne må endres"""
    def printSchedule(self, schedule, file):
        file.write('Schedule:\n')
        for event in schedule.getFinalSchedule():
            file.write('Event {e}, '.format(e = event.getNumber()))
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

        n, bins, patches = plt.hist(terminationDates, density = 100, facecolor = 'green')
        plt.title('Histogram of termination dates')
        plt.xlabel('Termination dates')
        plt.ylabel('Percentage')
        file = plt.savefig('terminationDateHistogram.pdf')
        return file

    def printHTML(self, terminationDates, bestTermination):
        self.plotTerminationDates(terminationDates)
        HTMLstring = """
        <html>
        <img src='terminationDateHistogram.pdf'>
        \n
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
            </head>
            <body>

            <h2>Table of best terminations</h2>
            <table>
            <tr>
                <th>Company</th>
                <th>Contact</th>
                <th>Country</th>
            </tr>
            <tr>
                <td>Alfreds Futterkiste</td>
                <td>Maria Anders</td>
                <td>Germany</td>
            </tr>
            
            </table>
            </body>
            </html>"""
        file = open("optimized.html","w")
        file.write(HTMLstring)
        file.close()


        