"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Normalization import Normalization
from ProjectPrediction import ProjectPrediction

""" Testing Task1 """

path = "projectData"
in_Normalization = Normalization()
predict = ProjectPrediction()
dictOfAllProjects = in_Normalization.readFiles(path) # read all files in this folder

"""in_Normalization.plotHistorgramOfDelays()"""

#------------------------------------------------------------------------------------------------------------

""" Testing Task 2 """
"""
# Here you can decide the # of weeks (in a precentage) you want to use (the number has to be a decimal)
classificationDf = in_Normalization.generateDataFrameForClassification(dictOfAllProjects, 0.2) 

# Here you can print put the dataframe to see how it looks like
print(classificationDf)

# In all three algorithms you can decide the test-split (in decimal)

# Logistic Regression 
predict.logisticReg(classificationDf, 0.2)

# KNeighbors 
predict.KNeighbors(classificationDf, 0.2)

# Naive Bayes 
predict.naiveBayes(classificationDf, 0.2)

# Decision Tree 
predict.decisionTree(classificationDf, 0.2)
"""

#------------------------------------------------------------------------------------------------------------

""" Testing Task 3 """

# Here you can decide the # of weeks you want to use (the number is a decimal)
"""regressionDf = in_Normalization.generateDataFrameForRegression(dictOfAllProjects, 0.05)

# Here you can print put the dataframe to see how it looks like
print(regressionDf)

# In all three algorithms you can decide the test-split (in decimal)

#Linear SVR 
predict.SVRlinear(in_Normalization, regressionDf, 0.2)

# Linear Lasso 
predict.LassoLinear(in_Normalization, regressionDf, 0.2)

# Ridge Regression 
predict.ridgeReg(in_Normalization, regressionDf, 0.2)"""
