"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

import math
import numpy as np
import pandas as pd 
import csv
from itertools import islice
from pprint import pprint
from sklearn import svm
from sklearn import metrics

class ParseProject:

    def __init__(self):
        self.projectName = None
        self.expectedDuration = None
        self.actualDuration = None
    
    # Q: In task 2.2 and 2.3; what is considered 'early'?
    # Q: Mate inn til maskinlæring: 
    # 1. prosent; expected duration / this week number
    # 2. prosent; summen av alle variabler / 800 

    #    Your first task consists thus in writting a Python script that normalizes the data, 
    #    i.e. that transforms their weekly progression into an abstract scale of progression.

    def importProjectPandas(self, fileName):
        expectedDurationDataFrame = pd.read_csv(fileName, sep='\t', nrows=1)
        expectedDuration = expectedDurationDataFrame.iat[0,1] 
        projectDataFrame = pd.read_csv(fileName, sep='\t', header=2)

        return projectDataFrame

    # Design one or more Python scripts to make statistics on how much projects are delayed. 
    # Q: From week to week, or in the end of the project?
    def calculateStatisticsOfProject(self, project):
        statList = []
    

    # In particular, print out histograms of delays.
    """def plotTerminationDates(self, terminationDates):
            minDate = np.amin(terminationDates)
            maxDate = np.max(terminationDates)

            n, bins, patches = plt.hist(terminationDates, rwidth=0.7, density = 50, facecolor = 'darkseagreen')
            plt.title('Histogram of termination dates')
            plt.xlabel('Termination date')
            plt.ylabel('Percentage of all terminations')
            file = plt.savefig('terminationDateHistogram.pdf')
            return file"""

    def setProjectName(self, projectName):
        self.projectName = projectName  
    
    def getProjectName(self):
        return self.projectName 

    def setExpectedDuration(self, expectedDuration):
        self.expectedDuration = int(expectedDuration)

    def getExpectedDuration(self):
        return self.expectedDuration 

    def setAcutalDuration(self, actualDuration):
        self.actualDuration = actualDuration
    
    def getAcutalDuration(self):
        return self.actualDuration 

    """def importProject(self, csv_file):
        try:
            inputFile = open(csv_file, 'r')
        except FileNotFoundError:
            print("The file " + csv_file + "does not exist.")
    
        #array = np.genfromtxt(islice(inputFile, 3, 5))
        content = [x.strip() for x in inputFile.readlines()] 
        newContent = []
        headers = []
        week = 0

        for i in range(len(content)):
            thisLine = content[i].split('\t')
            if i == 0:
                self.setProjectName(thisLine[1])
            elif i == 1:
                self.setExpectedDuration(thisLine[1])
            elif i == 2:
                headers = thisLine
            else: 
                floatLine = []
                for e in thisLine:
                    floatLine.append(float(e))
                week += 1
                newContent.append(floatLine)
            self.setAcutalDuration(week)
        return newContent"""


""" Testing """

parsing = ParseProject() 
print(parsing.importProjectPandas(r'projectData\project001.tsv'))

testContent = parsing.importProject(testFile)
print(parsing.getAcutalDuration())
