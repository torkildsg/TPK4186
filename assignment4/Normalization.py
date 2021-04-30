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
    
    def appendProject(self, projectName, df):
        self.allProjectDataFrames[projectName] = df

    def normalizeDataInColumns(self, projectDataFrame):
        scaling = MinMaxScaler()
        scaling.fit_transform(projectDataFrame[['Foundation'], ['Framing'], ['CurtainWall'], ['HVAC'], ['FireFighting'], ['Elevator'], ['Electrical'], ['ArchitecturalFinishing']])
        # Jobbe videre her 


    def createColumsForWeeklyProgression(self, projectCode):
        expectedDuration = self.getExpectedDuration()
        df = self.getProjectDataFrame()
        df = df.assign(WeeklyProgression=lambda x:(round((x['Week'] / expectedDuration), 4)))
        self.setProjectDataFrame(df)
    
     # Funkson for å hente alle filene
    def allProjects(self, directory):
        pathlist = Path("/Users/eivndlarsen/Documents/NTNU/Performance engineering /TPK4186/assignment4/projectData").rglob('*.tsv')
        for path in sorted(pathlist):
             # because path is object not string
             path_in_str = str(path)
             #print(path_in_str)

    def calculateWeeklyDelay(self, projectDataFrame):
        ...


    # Design one or more Python scripts to make statistics on how much projects are delayed. 
    # Q: From week to week, or in the end of the project?. 
    # Q: Make statistics for every project, and plot this, or what? 
    def calculateStatisticsOfProject(self, project):
        ...
    
    # Funkson for å hente alle filene

    def readFiles(self):
        pathlist = Path("/Users/eivndlarsen/Documents/NTNU/Performance engineering /TPK4186/assignment4/projectData").rglob('*.tsv')
        for path in sorted(pathlist):
            #because path is object not string
            path_in_str = str(path)
            #print(path_in_str)

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

