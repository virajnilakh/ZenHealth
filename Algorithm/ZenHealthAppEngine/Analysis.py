#Import Library
from time import time
import matplotlib.pyplot as plt

from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier

import pandas as pd
import numpy as np
import scipy as sp

from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


class Analysis():

    def main(self):
        X = pd.read_csv('./dataset/dataset.csv')
        Y = X['label']
        # preprocessing
        le = preprocessing.LabelEncoder()
        X_c = le.fit_transform(X['fooditem'])

        X = X.drop('fooditem', 1)

        X['fooditem'] = X_c

        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.30, random_state=99)

        print("X_train total length:", len(X_train))
        print("X_test total length:", len(X_test))
        print("Y_train total length:", len(y_train))

        model_nb = GaussianNB()
        model_svm = svm.SVC()
        model_lr = LogisticRegression()
        model_knn_centroid = NearestCentroid()
        model_knn = KNeighborsClassifier()
        eclf = VotingClassifier(
            estimators=[('lr', model_lr), ('knn_centroid', model_knn_centroid), ('gnb', model_nb), ('svc', model_svm),
                        ('knn', model_knn)],
            voting='hard', weights=[1, 1, 1, 1, 1])

        models = [model_nb, model_svm, model_lr, model_knn_centroid, model_knn, eclf]
        model_names = ["Naive Bayes", "SVM", "Logistic Regression", "Nearest Neighbors using Centroid",
                       "K-nearest Neighbors", "Ensemble"]

        best_model = None
        best_accuracy = 0
        best_preds = None

        print("Performance of models")
        print("======================")
        for model, name in zip(models, model_names):
            model.fit(X_train, y_train)
            preds = model.predict(X_test)
            accuracy = accuracy_score(y_test, preds)
            rmse_nb = mean_squared_error(y_test, preds)
            print("Name:", name)
            print("Accuracy score: ", accuracy)
            print("RMSE: ", rmse_nb)
            if accuracy >= best_accuracy:
                best_accuracy = accuracy
                best_model = model
                best_preds = preds

        print("======================")
        print("Best model:", best_model)
        print("Best accuracy:", best_accuracy)
        print("Best predictions:", best_preds)

        results = X_train
        X_test = X_test.drop('label', 1)
        X_test['label'] = best_preds
        results.append(X_test)
        #convert fooditem nos into string
        X_d = le.inverse_transform(results['fooditem'])
        print(X_d)
        results = results.drop('fooditem', 1)
        results['fooditem'] = X_d
        return results


    def getLowBucket(self):

        results = self.main()
        food_bucket = results.loc[(results['label'] == 1)]
        food_bucket = food_bucket.sort_values(['sugars'], ascending=[True])
        print(" Low sugar food bucket:", len(food_bucket))
        print(" Total food items")
        print("============")
        low_bucket = food_bucket[['fooditem', 'sugars']]
        return low_bucket


    def getMediumBucket(self):

        results = self.main()
        food_bucket = results.loc[(results['label'] == 2)]
        food_bucket = food_bucket.sort_values(['sugars'], ascending=[True])
        print(" Medium sugar food bucket:", len(food_bucket))
        print(" Total food items")
        print("============")
        medium_bucket = food_bucket[['fooditem', 'sugars']]
        return medium_bucket

    def getHighBucket(self):

        results = self.main()
        food_bucket = results.loc[(results['label'] == 3)]
        food_bucket = food_bucket.sort_values(['sugars'], ascending=[True])
        print(" High sugar food bucket:", len(food_bucket))
        print(" Total food items")
        print("============")
        high_bucket = food_bucket[['fooditem', 'sugars']]
        return high_bucket


