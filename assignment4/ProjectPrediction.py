"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Normalization import Normalization
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import math
from sklearn import svm, metrics, preprocessing, linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

class ProjectPrediction:
    def __init__(self):
        super().__init__()

    """ Task 2: Classification algorithms """

    def logisticReg(self, df, testSize):
        # Seperate our columns into X (features), y (target labels)
        X, y = df.drop(['Project', 'FiascoBinary'], axis=1), df['FiascoBinary'].astype('int')

        # Split our data with a certain train/test-split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = testSize)

        lr_model = LogisticRegression()
        lr_model.fit(X_train,y_train)
        train_prediction = lr_model.predict(X_train)

        train_acc = accuracy_score(y_train, train_prediction)
        print(f"Logistic Regression: \nAccuracy on training data: {train_acc:.4f}")
        
        # Predict test data
        test_prediction = lr_model.predict(X_test)

        # Calculate accuracy on test set
        test_acc = accuracy_score(y_test, test_prediction)
        print(f"Accuracy on test data: {test_acc:.4f}\n")
        return ""
    
    def KNeighbors(self, df, testSize):
        X, y = df.drop(['Project', 'FiascoBinary'], axis=1), df['FiascoBinary'].astype('int')
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = testSize)

        knn_model = KNeighborsClassifier()
        knn_model.fit(X_train, y_train)
        train_prediction = knn_model.predict(X_train)
        train_acc = accuracy_score(y_train, train_prediction)
        print(f"KNeighbors: \nAccuracy on training data: {train_acc:.4f}")

        test_prediction = knn_model.predict(X_test)
        test_acc = accuracy_score(y_test, test_prediction)
        print(f"Accuracy on test data: {test_acc:.4f}\n")
        return ""
    
    def naiveBayes(self, df, testSize):
        X, y = df.drop(['Project', 'FiascoBinary'], axis=1), df['FiascoBinary'].astype('int')
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = testSize)

        gnb_model = GaussianNB()
        gnb_model.fit(X_train, y_train)
        train_prediction = gnb_model.predict(X_train)
        train_acc = accuracy_score(y_train, train_prediction)
        print(f"Naive Bayes: \nAccuracy on training data: {train_acc:.4f}")

        test_prediction = gnb_model.predict(X_test)
        test_acc = accuracy_score(y_test, test_prediction)
        print(f"Accuracy on test data: {test_acc:.4f}\n")
        return ""
    
    def decisionTree(self, df, testSize):
        X, y = df.drop(['Project', 'FiascoBinary'], axis=1), df['FiascoBinary'].astype('int')
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = testSize)

        dt_model = DecisionTreeClassifier()
        dt_model.fit(X_train, y_train)
        train_prediction = dt_model.predict(X_train)
        train_acc = accuracy_score(y_train, train_prediction)
        print(f"Decision tree: \nAccuracy on training data: {train_acc:.4f}")

        test_prediction = dt_model.predict(X_test)
        test_acc = accuracy_score(y_test, test_prediction)
        print(f"Accuracy on test data: {test_acc:.4f}\n")
        return ""

    """ Task 3: Regression algorithms """

    def SVRlinear(self, normalization, df, testSize):
        X, y = df.drop(['Project', 'ActualDuration'], axis=1), df['ActualDuration'].astype('int')
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = testSize)

        linear_model = svm.SVR(kernel="linear")
        linear_model.fit(X_train, y_train)
        train_prediction = linear_model.predict(X_train)
        test_prediction = linear_model.predict(X_test)

        print("SVR linear prediction with " + str(normalization.percentageOfWeeksRegression*100) + "% of the data in each of the " + str(len(normalization.allProjectDataFrames)) + \
            " projects, \nand a train/test ratio of " + str(int((1-testSize)*100)) + "/" + str(int(testSize*100)) + " resulted in:")
        print("MAE:\t{0:.3f}".format(metrics.mean_absolute_error(y_test, test_prediction)))
        print("RMSE:\t{0:.3f}".format(metrics.mean_squared_error(y_test, test_prediction, squared=False)))
        print("R^2:\t{0:>1.3f}\n".format(metrics.r2_score(y_test, test_prediction)))
        return ""

    def LassoLinear(self, normalization, df, testSize):
        X, y = df.drop(['Project', 'ActualDuration'], axis=1), df['ActualDuration'].astype('int')
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = testSize)

        lasso_model = linear_model.Lasso(alpha=0.01)
        lasso_model.fit(X_train, y_train) 
        train_prediction = lasso_model.predict(X_train)
        test_prediction = lasso_model.predict(X_test)

        print("Lasso linear prediction with " + str(normalization.percentageOfWeeksRegression*100) + "% of the data in each of the " + str(len(normalization.allProjectDataFrames)) + \
            " projects, \nand a train/test ratio of " + str(int((1-testSize)*100)) + "/" + str(int(testSize*100)) + " resulted in:")
        print("MAE:\t{0:.3f}".format(metrics.mean_absolute_error(y_test, test_prediction)))
        print("RMSE:\t{0:.3f}".format(metrics.mean_squared_error(y_test, test_prediction, squared=False)))
        print("R^2:\t{0:>1.3f}\n".format(metrics.r2_score(y_test, test_prediction)))
        return ""
    
    def ridgeReg(self, normalization, df, testSize):
        X, y = df.drop(['Project', 'ActualDuration'], axis=1), df['ActualDuration'].astype('int')
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = testSize)

        ridge_model = linear_model.Ridge(alpha=.5)
        ridge_model.fit(X_train, y_train)
        train_prediction = ridge_model.predict(X_train)
        test_prediction = ridge_model.predict(X_test)

        print("Ridge regression prediction with " + str(normalization.percentageOfWeeksRegression*100) + "% of the data in each of the " + str(len(normalization.allProjectDataFrames)) + \
            " projects, \nand a train/test ratio of " + str(int((1-testSize)*100)) + "/" + str(int(testSize*100)) + " resulted in:")
        print("MAE:\t{0:.3f}".format(metrics.mean_absolute_error(y_test, test_prediction)))
        print("RMSE:\t{0:.3f}".format(metrics.mean_squared_error(y_test, test_prediction, squared=False)))
        print("R^2:\t{0:>1.3f}\n".format(metrics.r2_score(y_test, test_prediction)))
        return ""