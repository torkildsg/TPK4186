"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Normalization import Normalization
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd 
from sklearn import svm, metrics, preprocessing
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB


# A project is considered as a fiasco if its actual duration is at least 40% higher than its expected
# duration. Using different classification algorithms (at least 3), study whether it is possible detect
# early that a project will be a fiasco.

class FiascoDetection:
    def __init__(self):
        super().__init__()
    
    # Classification: We have <100K samples. 
    # Try:
    #   1. Logistic SVR
    #   2. Naive Bayes
    #   3. KNeighbors Classifier

    # Regression: We have <100K samples
    # Try: 
    #   1. RidgeRegression
    #   2. SVR(kernel = 'linear')
    #   3. SVR(kernel = 'rbf')
    #   4. EnsembleRegressors

    """ Task 2: Classification algorithms """

    def logisticReg(self, df, testSize):
        # Seperate our columns into X (features), y (target labels)
        X, y = df.drop(['WeeklyProgression', 'Week', 'FiascoBinary'], axis=1), df['FiascoBinary'] # .values

        # Split our data with a 50/50 train/test-split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = testSize)

        lr_model = LogisticRegression()
        lr_model.fit(X_train,y_train)
        train_prediction = lr_model.predict(X_train)

        train_acc = accuracy_score(y_train, train_prediction)
        print(f"Accuracy on training data: {train_acc:.4f}")
        
        # Predict test data
        test_prediction = lr_model.predict(X_test)

        # Calculate accuracy on test set
        test_acc = accuracy_score(y_test, test_prediction)
        print(f"Accuracy on test data: {test_acc:.4f}")
    
    def KNeighbors(self, df, testSize):
        X, y = df.drop(['WeeklyProgression', 'Week', 'FiascoBinary'], axis=1), df['FiascoBinary'] # .values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = testSize)

        knn_model = KNeighborsClassifier()
        knn_model.fit(X_train, y_train)
        train_prediction = knn_model.predict(X_train)

        # Output accuracy on training data
        train_acc = accuracy_score(y_train, train_prediction)
        print(f"Accuracy on training data: {train_acc:.4f}")

        # Predict test data
        test_prediction = knn_model.predict(X_test)

        # Calculate accuracy on test set
        test_acc = accuracy_score(y_test, test_prediction)
        print(f"Accuracy on test data: {test_acc:.4f}")
    
    def naiveBayes(self, df, testSize):
        X, y = df.drop(['WeeklyProgression', 'Week', 'FiascoBinary'], axis=1), df['FiascoBinary'] # .values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = testSize)

        gnb_model = GaussianNB()
        gnb_model.fit(X_train, y_train)
        train_prediction = gnb_model.predict(X_train)
        
        # Output accuracy on training data
        train_acc = accuracy_score(y_train, train_prediction)
        print(f"Accuracy on training data: {train_acc:.4f}")

        # Predict test data
        test_prediction = gnb_model.predict(X_test)

        # Calculate accuracy on test set
        test_acc = accuracy_score(y_test, test_prediction)
        print(f"Accuracy on test data: {test_acc:.4f}")
    

    """ Task 3: Regression algorithms """

    def RidgeReg(self, df, testSize):
        ...
    
    def SVRlinear(self, df, testSize):
        ...
    
    def SVRrbf(self, df, testSize):
        ...