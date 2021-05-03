"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

import numpy as np
import pandas as pd

class Project:
    def __init__(self, projectCode, fileName):
        self.projectCode = projectCode
        self.fileName = fileName
        self.expectedDuration = None
        self.actualDuration = None
        self.projectDataFrame = None
        self.importProject(fileName)
    
    def getProject(self, projectCode):
        return self.projectCode
    
    def getProjectCode(self):
        return self.projectCode

    def importProject(self, fileName):
        expectedDurationDataFrame = pd.read_csv(fileName, sep='\t', nrows=1)
        expectedDuration = expectedDurationDataFrame.iat[0,1] 
        projectDataFrame = pd.read_csv(fileName, sep='\t', header=2)

        self.setExpectedDuration(expectedDuration) 
        self.setProjectDataFrame(projectDataFrame) 
        return projectDataFrame
    
    def getDelay(self):
        return round((self.getActualDuration()/self.getExpectedDuration()), 3)
         
    def setExpectedDuration(self, expectedDuration):
        self.expectedDuration = int(expectedDuration)

    def getExpectedDuration(self):
        return self.expectedDuration 

    def setActualDuration(self):
        df = self.getProjectDataFrame()
        actualWeek = df.iloc[-1]['Week']
        self.actualDuration = actualWeek
    
    def getActualDuration(self):
        return self.actualDuration 
    
    def setProjectDataFrame(self, dataframe):
        self.projectDataFrame = dataframe
    
    def getProjectDataFrame(self):
        return self.projectDataFrame