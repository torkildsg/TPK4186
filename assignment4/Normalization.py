"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

import math
import numpy as np
import pandas as pd 
import csv
from itertools import islice
from pprint import pprint

"""from sklearn import svm
from sklearn import metrics"""

class ParseProject:
    def __init__(self):

        self.projectName = None
        self.expectedDuration = None
        self.actualDuration = None

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

    def importProject(self, csv_file):
    
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

        return newContent


    
    
    

    


""" Testing """


testFile = "/Users/eivndlarsen/Documents/NTNU/Performance engineering /TPK4186/assignment4/projectData/project001.tsv"

parsing = ParseProject() 


testContent = parsing.importProject(testFile)
print(parsing.getAcutalDuration())
