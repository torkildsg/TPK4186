"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Normalization import Normalization
from ProjectPrediction import ProjectPrediction

""" Testing Task1 """

eivindPath = "/Users/eivndlarsen/Documents/NTNU/Performance engineering /TPK4186/assignment4/projectData"
torkildPath = "projectData"

in_Normalization = Normalization()
dictOfAllProjects = in_Normalization.readFiles(torkildPath)
#in_Normalization.plotHistorgramOfDelays()


""" Testing Task 2 """

# All projects that is a fiasco: 15, 28, 40, 47, 60, 76
# Here you can decide the # of weeks you want to use (the number is a decimal)
normalizedDf = in_Normalization.generateDataFrameForClassification(dictOfAllProjects, 0.2) 
print(normalizedDf)
print(normalizedDf.iloc[[39]])

predict = ProjectPrediction()

""" Testing Logistic Regression """
# Here you can decide the test-split (in decimal)
print("Logistic Regression: ")
print(predict.logisticReg(normalizedDf, 0.7))
print("\n")

""" Testing KNeighbors """
print("KNeighbors: ")
print(predict.KNeighbors(normalizedDf, 0.7))
print("\n")

""" Testing Naive Bayes """
print("Naive Bayes: ")
print(predict.naiveBayes(normalizedDf, 0.7))
print("\n")