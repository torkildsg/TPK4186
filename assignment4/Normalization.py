"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

import math
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import csv
import seaborn as sns
#from itertools import islice
#from pprint import pprint
from sklearn import svm, metrics
from sklearn.preprocessing import MinMaxScaler
from pathlib import Path
from Project import Project




class Normalization:

    def __init__(self):
        self.allProjectDataFrames = dict() # {key: 'project001', values: <df>, ...}
    
    # Q: In task 2.2 and 2.3; what is considered 'early'?
    # A: Mater inn data, records fra uke til uke, hvor tidlig klarer man av å avgjøre hvorvidt det er en fiasko?
    # Prøv å begrense litt og litt data

    # Q: Mate inn til maskinlæring: 
    # 1. prosent; expected duration / this week number A: JA, bruk denne. Denne vil gi forventet prosent

    #    Your first task consists thus in writting a Python script that normalizes the data, 
    #    i.e. that transforms their weekly progression into an abstract scale of progression.
    
    def appendProject(self, project, df):
        self.allProjectDataFrames[project] = df

    def calculateProjectDelay(self, project):
        lastWeek = project.getProjectDataFrame().iloc[-1]['Week']

    def normalizeDataInColumns(self, project):
        thisDf = project.getProjectDataFrame()
        scaling = MinMaxScaler()
        normalizedDataframe = scaling.fit_transform(thisDf[['Foundation'], ['Framing'], ['CurtainWall'], ['HVAC'], ['FireFighting'], ['Elevator'], ['Electrical'], ['ArchitecturalFinishing']]) 
        project.setProjectDataFrame(normalizedDataframe)
        return normalizedDataframe

    def createColumnsForWeeklyProgression(self, project):
        expectedDuration = project.getExpectedDuration()
        df = project.getProjectDataFrame()
        df = df.assign(WeeklyProgression=lambda x:(round((x['Week'] / expectedDuration), 4)))
        project.setProjectDataFrame(df)

    
    # Funkson for å hente alle filene
    def readFiles(self, folderPath):
        pathlist = Path(str(folderPath)).rglob('*.tsv')
        for path in sorted(pathlist):
            pathString = str(path)
            print(pathString)
            start = 'projectData/project'
            end = '.tsv'
            projectCode = int((pathString.split(start))[1].split(end)[0])
            newProject = Project(projectCode, pathString)
            self.createColumnsForWeeklyProgression(newProject)
            self.normalizeDataInColumns(newProject)
            self.appendProject(newProject, newProject.getProjectDataFrame())


    # In particular, print out histograms of delays. 
    # Q: For all projects in general?

    """def plotTerminationDates(self, terminationDates):
            minDate = np.amin(terminationDates)
            maxDate = np.max(terminationDates)

            n, bins, patches = plt.hist(terminationDates, rwidth=0.7, density = 50, facecolor = 'darkseagreen')
            plt.title('Histogram of termination dates')
            plt.xlabel('Termination date')
            plt.ylabel('Percentage of all terminations')
            file = plt.savefig('terminationDateHistogram.pdf')
            return file"""
  



""" Testing """

eivindPath = "/Users/eivndlarsen/Documents/NTNU/Performance engineering /TPK4186/assignment4/projectData"
#torkildPath = "\Users\Torkild\TPK4186\assignment4\projectData"

in_Normalization = Normalization()
in_Normalization.readFiles(torkildPath)

print(in_Normalization.allProjectDataFrames)

