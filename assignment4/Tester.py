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

"""for key, value in in_Normalization.allProjectDataFrames.items():
    print(value)
    print('\n')
"""    

# All projects that is a fiasco: 15, 28, 40, 47, 60, 76
detect = FiascoDetection()
test15 = list(in_Normalization.allProjectDataFrames.values())[14]
test28 = list(in_Normalization.allProjectDataFrames.values())[27]
test40 = list(in_Normalization.allProjectDataFrames.values())[39]
test47 = list(in_Normalization.allProjectDataFrames.values())[46]
test60 = list(in_Normalization.allProjectDataFrames.values())[59]
test76 = list(in_Normalization.allProjectDataFrames.values())[75]

print(detect.logisticReg(test15))
