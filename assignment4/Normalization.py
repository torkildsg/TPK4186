"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

import math
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import csv
from sklearn import svm, metrics, preprocessing
from sklearn.preprocessing import MinMaxScaler
from pathlib import Path
from Project import Project


class Normalization:

    def __init__(self):
        self.allProjectDataFrames = dict() # {key: <Project>, values: <df>, ...}
        self.allProjectDelays = []
    
    # Q: In task 2.2 and 2.3; what is considered 'early'?
    # A: Mater inn data, records fra uke til uke, hvor tidlig klarer man av å avgjøre hvorvidt det er en fiasko?
    # Prøv å begrense litt og litt data

    # Q: Mate inn til maskinlæring: 
    # 1. prosent; expected duration / this week number A: JA, bruk denne. Denne vil gi forventet prosent

    #    Your first task consists thus in writting a Python script that normalizes the data, 
    #    i.e. that transforms their weekly progression into an abstract scale of progression.
    
    def getAllProjectsDelays(self):
        return self.allProjectDelays
    
    def appendProject(self, project, df):
        self.allProjectDataFrames[project] = df



    def calculateAllProjectsDelay(self):
        for key, value in self.allProjectDataFrames.items():    
            key.setActualDuration()
            delay = round(float((key.getDelay()-1)*100), 1)
            self.allProjectDelays.append(delay)
        return self.getAllProjectsDelays

    def normalizeDataInColumns(self, project):
        df = project.getProjectDataFrame()
        scaling = MinMaxScaler()
        df[['Foundation', 'Framing', 'CurtainWall', 'HVAC', 'FireFighting', 'Elevator', 'Electrical', 'ArchitecturalFinishing']] = scaling.fit_transform(df[['Foundation', 'Framing', 'CurtainWall', 'HVAC', 'FireFighting', 'Elevator', 'Electrical', 'ArchitecturalFinishing']])
        project.setProjectDataFrame(df)
        return df

    def createColumnsForWeeklyProgression(self, project):
        expectedDuration = project.getExpectedDuration()
        df = project.getProjectDataFrame()
        df = df.assign(WeeklyProgression=lambda x:(round((x['Week'] / expectedDuration), 3)))
        project.setProjectDataFrame(df)
    

    def createBinaryFiasco(self, project):
        df = project.getProjectDataFrame()
        """conditionOne = (df["WeeklyProgression"] < 1.4) 
        conditionTwo = (df["WeeklyProgression"] >= 1.4)
        conditions = [conditionOne, conditionTwo]
        choices = [0, 1]
        df["FiascoBinary"] = np.select(conditions, choices)"""
        if project.getDelay() >= 1.4:
            df["FiascoBinary"] = 1
        else:
            df["FiascoBinary"] = 0 

    
    # Funkson for å hente alle filene
    def readFiles(self, folderPath):
        pathlist = Path(str(folderPath)).rglob('*.tsv')
        for path in sorted(pathlist):
            pathString = str(path)
            mac = 'projectData/project'
            if mac in pathString:
                start = mac
            else:
                start = 'projectData\project'
            end = '.tsv'
            projectCode = int((pathString.split(start))[1].split(end)[0])
            newProject = Project(projectCode, pathString)
            self.createColumnsForWeeklyProgression(newProject)
            newProject.setActualDuration()
            self.createBinaryFiasco(newProject)
            self.normalizeDataInColumns(newProject)
            self.appendProject(newProject, newProject.getProjectDataFrame())
        self.calculateAllProjectsDelay()


    # In particular, print out histograms of delays. 
    def plotHistorgramOfDelays(self):
        listOfDelays = self.getAllProjectsDelays()
        minDelay = np.amin(listOfDelays)
        maxDelay = np.max(listOfDelays)

        fig, ax = plt.subplots(1, figsize=(8,4))
        n, bins, patches = plt.hist(listOfDelays, rwidth=0.7, density = True, facecolor = 'darkseagreen', bins=np.arange(min(listOfDelays), max(listOfDelays), 10))
        plt.title('Histogram of Project-delays')

        # x-ticks
        xticks = [(bins[idx+1] + value)/2 for idx, value in enumerate(bins[:-1])]
        xticks_labels = [ "{:.0f}-{:.0f}".format(value, bins[idx+1]) for idx, value in enumerate(bins[:-1])]
        plt.xticks(xticks, labels = xticks_labels, fontsize=8)
        ax.tick_params(axis='x', which='both',length=0)
        
        plt.xlabel('Delay [%]')
        plt.ylabel('Percentage')
        file = plt.savefig('delayHistogram.pdf')
        return file


