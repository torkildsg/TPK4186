"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Normalization import Normalization
from FiascoDetection import FiascoDetection

def getAllActualFiascoprojects():
    for key, value in in_Normalization.allProjectDataFrames.items():
        if float(key.getActualDuration()/key.getExpectedDuration()) >= float(1.4):
            print("Project: "+ str(key.getProjectCode())+ " - "+ str(float(key.getActualDuration()/key.getExpectedDuration()) >= float(1.4)))
            print('\n')


""" Testing """

eivindPath = "/Users/eivndlarsen/Documents/NTNU/Performance engineering /TPK4186/assignment4/projectData"
torkildPath = "projectData"

in_Normalization = Normalization()
in_Normalization.readFiles(eivindPath)
in_Normalization.calculateAllProjectsDelay()
in_Normalization.plotHistorgramOfDelays()




"""detect = FiascoDetection()
testDf = list(in_Normalization.allProjectDataFrames.values())[0]
print(testDf)
print(detect.logisticRegression(testDf))"""

#getAllActualFiascoprojects()