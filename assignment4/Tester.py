"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Normalization import Normalization
from ProjectPrediction import ProjectPrediction

""" Testing Task1 """

path = "projectData"

in_Normalization = Normalization()
dictOfAllProjects = in_Normalization.readFiles(path)
#in_Normalization.plotHistorgramOfDelays()

#------------------------------------------------------------------------------------------------------------

""" Testing Task 2 """
# All projects that is a fiasco: 15, 28, 40, 47, 60, 76
# Here you can decide the # of weeks you want to use (the number is a decimal)
classificationDf = in_Normalization.generateDataFrameForClassification(dictOfAllProjects, 0.2) 
predict = ProjectPrediction()

# Here you can print put the dataframe to see how it looks like
print(classificationDf)

""" Testing Logistic Regression """
# Here you can decide the test-size (in decimal)
#predict.logisticReg(classificationDf, 0.2)

""" Testing KNeighbors """
#predict.KNeighbors(classificationDf, 0.2)

""" Testing Naive Bayes """
#predict.naiveBayes(classificationDf, 0.2)

""" Testing Decision Tree """
#predict.decisionTree(classificationDf, 0.20)

#------------------------------------------------------------------------------------------------------------

""" Testing Task 3 """
# Here you can decide the # of weeks you want to use (the number is a decimal)
regressionDf = in_Normalization.generateDataFrameForRegression(dictOfAllProjects, 0.2)

# Here you can print put the dataframe to see how it looks like
#print(regressionDf)

""" Testing Linear SVR """
# Here you can decide the test-split (in decimal)
#predict.SVRlinear(regressionDf, 0.2)

""" Testing Linear Lasso """
#predict.LassoLinear(regressionDf, 0.2)

""" Testing Ridge Regression """
#predict.ridgeReg(regressionDf, 0.2)
