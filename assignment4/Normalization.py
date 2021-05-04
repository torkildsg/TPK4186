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
        self.normalizedDataFrameForClassification = None # The dataframe containing all the projects status after a certain time (..given in %)
        self.setNormalizedDataFrameForClassification()
        self.normalizedDataFrameForRegression = None
        self.setNormalizedDataFrameForRegression()

    def setNormalizedDataFrameForClassification(self):
        df = pd.DataFrame(columns = ['Project', 'Foundation', 'Framing', 'CurtainWall', 'HVAC', 'FireFighting', 'Elevator', 'Electrical', 'ArchitecturalFinishing', 'FiascoBinary'])
        self.normalizedDataFrameForClassification = df
    
    def getNormalizedDataFrameForClassification(self):
        return self.normalizedDataFrameForClassification

    def setNormalizedDataFrameForRegression(self):
        df = pd.DataFrame(columns = ['Project', 'Week', 'Foundation', 'Framing', 'CurtainWall', 'HVAC', 'FireFighting', 'Elevator', 'Electrical', 'ArchitecturalFinishing', 'ActualDuration'])
        self.normalizedDataFrameForRegression = df
    
    def getNormalizedDataFrameForRegression(self):
        return self.normalizedDataFrameForRegression

    def getAllProjectsDelays(self):
        return self.allProjectDelays

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
    
    def appendProject(self, project, df):
        self.allProjectDataFrames[project] = df
    
    def generateDataFrameForClassification(self, dictOfAllProjects, percentageOfTime):
        for key, value in dictOfAllProjects.items():
            rowNumber = int(math.ceil(key.getActualDuration() * percentageOfTime)-1)
            df = value.drop(['Week'], axis=1).iloc[[rowNumber]]
            df.insert(0, 'Project', 'Project' + str(key.getProjectCode()))
            self.normalizedDataFrameForClassification = self.normalizedDataFrameForClassification.append(df.iloc[[0]], ignore_index=True)
        return self.normalizedDataFrameForClassification
    
    def generateDataFrameForRegression(self, dictOfAllProjects, percentageOfTime):
        for key, value in dictOfAllProjects.items():
            rowNumber = int(math.ceil(key.getActualDuration() * percentageOfTime)-1)
            df = value.drop(['FiascoBinary'], axis=1).iloc[[rowNumber]]
            df.insert(0, 'Project', 'Project' + str(key.getProjectCode()))
            df['ActualDuration'] = key.getActualDuration() #round(float(key.getActualDuration()/key.getExpectedDuration()), 4)
            self.normalizedDataFrameForRegression = self.normalizedDataFrameForRegression.append(df.iloc[[0]], ignore_index=True)
        return self.normalizedDataFrameForRegression

    def createFiascoBinary(self, project):
        df = project.getProjectDataFrame()
        if project.getDelay() >= 1.4:
            df["FiascoBinary"] = 1
        else:
            df["FiascoBinary"] = 0
    
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
            newProject.setActualDuration()
            self.createFiascoBinary(newProject) 
            self.normalizeDataInColumns(newProject)
            self.appendProject(newProject, newProject.getProjectDataFrame())
        self.calculateAllProjectsDelay()
        return self.allProjectDataFrames


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