"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

import math
import numpy as np
import pandas as pd 
import csv
from sklearn import svm
from sklearn import metrics

# Q: In task 2.2 and 2.3; what is considered 'early'?
# Q: Mate inn til maskinlæring: 
# 1. prosent; expected duration / this week number
# 2. prosent; summen av alle variabler / 800 



#    Your first task consists thus in writting a Python script that normalizes the data, 
#    i.e. that transforms their weekly progression into an abstract scale of progression.

def importProjectPandas(fileName):
    expectedDurationDataFrame = pd.read_csv(fileName, sep='\t', nrows=1)
    expectedDuration = expectedDurationDataFrame.iat[0,1] 
    projectDataFrame = pd.read_csv(fileName, sep='\t', header=2)


    return projectDataFrame

# 0 = week 1
# projectDict.get('foundation')[1] + projectDict.get('framing')[1] + projectDict.get('curtainWall')[1] + projectDict.get('framing')[1]
def progressionTillThisWeek(weekNumber, projectList):
    weekNumber -= 1
    thisWeek = projectList[weekNumber]
    #thisWeek
    #numerator = sum(thisWee)

def totalWeeklyProgression(projectList): 
    ...

    #for keys, values in projectDict.items():


# Design one or more Python scripts to make statistics on how much projects are delayed. 
# Q: From week to week, or in the end of the project?
def calculateStatisticsOfProject(project):
    statList = []
    

# In particular, print out histograms of delays.
def plotTerminationDates(self, terminationDates):
        minDate = np.amin(terminationDates)
        maxDate = np.max(terminationDates)

        n, bins, patches = plt.hist(terminationDates, rwidth=0.7, density = 50, facecolor = 'darkseagreen')
        plt.title('Histogram of termination dates')
        plt.xlabel('Termination date')
        plt.ylabel('Percentage of all terminations')
        file = plt.savefig('terminationDateHistogram.pdf')
        return file


print(importProjectPandas(r'projectData\project001.tsv'))