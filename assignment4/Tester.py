"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Normalization import Normalization
from ProjectPrediction import ProjectPrediction

""" Testing Task1 """

eivindPath = "/Users/eivndlarsen/Documents/NTNU/Performance engineering /TPK4186/assignment4/projectData"
torkildPath = "projectData"

in_Normalization = Normalization()
dictOfAllProjects = in_Normalization.readFiles(torkildPath)
#in_Normalization.plotHistorgramOfDelays()

#------------------------------------------------------------------------------------------------------------

""" Testing Task 2 """
# All projects that is a fiasco: 15, 28, 40, 47, 60, 76
# Here you can decide the # of weeks you want to use (the number is a decimal)
classificationDf = in_Normalization.generateDataFrameForClassification(dictOfAllProjects, 0.2) 
predict = ProjectPrediction()

#print(classificationDf)
#print(classificationDf.iloc[[39]])

""" Testing Logistic Regression """
# Here you can decide the test-size (in decimal)
print(predict.logisticReg(classificationDf, 0.2))

""" Testing KNeighbors """
print(predict.KNeighbors(classificationDf, 0.2))

""" Testing Naive Bayes """
print(predict.naiveBayes(classificationDf, 0.2))

#------------------------------------------------------------------------------------------------------------

""" Testing Task 3 """
# Here you can decide the # of weeks you want to use (the number is a decimal)
regressionDf = in_Normalization.generateDataFrameForRegression(dictOfAllProjects, 0.2)
#print(regressionDf)

""" Testing Linear SVR """
# Here you can decide the test-split (in decimal)
predict.SVRlinear(regressionDf, 0.2)

""" Testing Linear Lasso """
predict.LassoLinear(regressionDf, 0.2)

""" Testing Ridge Regression """
predict.ridgeReg(regressionDf, 0.2)
