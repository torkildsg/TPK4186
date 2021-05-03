"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Normalization import Normalization
from FiascoDetection import FiascoDetection

""" Testing Task1 """

eivindPath = "/Users/eivndlarsen/Documents/NTNU/Performance engineering /TPK4186/assignment4/projectData"
torkildPath = "projectData"

in_Normalization = Normalization()
dictOfAllProjects = in_Normalization.readFiles(torkildPath)
#in_Normalization.plotHistorgramOfDelays()


""" Testing Task 2 """

# All projects that is a fiasco: 15, 28, 40, 47, 60, 76
# Here you can decide the # of weeks you want to use (the number is a decimal)
normalizedDf = in_Normalization.generateDataFrame(dictOfAllProjects, 0.3) 
print(normalizedDf)
print(normalizedDf.iloc[[39]])

detect = FiascoDetection()

""" Testing Logistic Regression """
# Here you can decide the train/test-split (in decimal)
print("Logistic Regression: ")
print(detect.logisticReg(normalizedDf, 0.5))
print("\n")

""" Testing KNeighbors """
print("KNeighbors: ")
print(detect.KNeighbors(normalizedDf, 0.5))
print("\n")

""" Testing Naive Bayes """
print("Naive Bayes: ")
print(detect.naiveBayes(normalizedDf, 0.5))
print("\n")