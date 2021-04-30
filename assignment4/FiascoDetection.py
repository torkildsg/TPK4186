"""" Group 14: Eivind Stangebye Larsen and Torkild Sandnes Grøstad """

from Normalization import Normalization
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# A project is considered as a fiasco if its actual duration is at least 40% higher than its expected
# duration. Using different classification algorithms (at least 3), study whether it is possible detect
# early that a project will be a fiasco.

class FiascoDetection:
    def __init__(self):
        super().__init__()

    def logisticRegression(self, df):
        X = df.drop(['WeeklyProgression', 'Week'], axis=1) 
        y = df['WeeklyProgression']

        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.25)
        model = LogisticRegression()
        model.fit(X_train,y_train)
        #lr_preds = lr.predict(X_test)
