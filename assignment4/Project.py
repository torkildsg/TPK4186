"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

import numpy as np
import pandas as pd

class Project:
    def __init__(self, name, fileName):
        self.projectName = name
        self.fileName = fileName
        self.expectedDuration = None
        self.actualDuration = None
        self.projectDataFrame = None
        self.importProject(fileName)
    
    def getProject(self, projectName):
        return self

    def importProject(self, fileName):
        expectedDurationDataFrame = pd.read_csv(fileName, sep='\t', nrows=1)
        expectedDuration = expectedDurationDataFrame.iat[0,1] 
        projectDataFrame = pd.read_csv(fileName, sep='\t', header=2)

        self.setExpectedDuration(expectedDuration) 
        self.setProjectDataFrame(projectDataFrame) 
        return projectDataFrame
    
    def setProjectName(self, projectName):
        self.projectName = projectName  
    
    def getProjectName(self):
        return self.projectName 

    def setExpectedDuration(self, expectedDuration):
        self.expectedDuration = int(expectedDuration)

    def getExpectedDuration(self):
        return self.expectedDuration 

    def setActualDuration(self, actualDuration):
        self.actualDuration = actualDuration
    
    def getActualDuration(self):
        return self.actualDuration 
    
    def setProjectDataFrame(self, dataframe):
        self.projectDataFrame = dataframe
    
    def getProjectDataFrame(self):
        return self.projectDataFrame