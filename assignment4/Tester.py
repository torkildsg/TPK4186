"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Normalization import Normalization
from FiascoDetection import FiascoDetection

""" Testing """

eivindPath = "/Users/eivndlarsen/Documents/NTNU/Performance engineering /TPK4186/assignment4/projectData"
torkildPath = "projectData"

in_Normalization = Normalization()
in_Normalization.readFiles(torkildPath)
in_Normalization.calculateAllProjectsDelay()
in_Normalization.plotHistorgramOfDelays()

for key, value in in_Normalization.allProjectDataFrames.items():
    print(value)
    print('\n')
    break

"""detect = FiascoDetection()
testDf = list(in_Normalization.allProjectDataFrames.values())[0]
print(testDf)
print(detect.logisticRegression(testDf))"""
