from flask import Flask, render_template, request, session, flash, redirect, jsonify, json, Response
from flask_restful import Resource, Api



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

import json
from pandas.io.json import json_normalize

import resources.datamanager as datamanager

# Algorithm
'''
connect to user profile  and get diet 
connect to db and get food details based on diet and time
'''
class API():

    def getBreakfast(self,userid):
        print("fetching breakfast")
        result = datamanager.food_db.get('/foodData', None)
        user = datamanager.user_db.get('/userProfile', userid)
        print(len(result))
        print(result)

        snapshot = datamanager.user_db_ref.order_by_child('uname').equal_to('arpi.dixit91@gmail.com').get()
        for key in snapshot:
            print(key)
        print(user)
        diet = user.get('diet')
        m = user.get('height') * 30.48 * 0.01
        print(m)
        kg = pound2kg(int(user.get('weight')))
        print(kg)
        bmi = round(kg / (m * m))
        print("Your body mass index is: ", bmi)
        if bmi <= 18.5:
            print('Your BMI is', bmi, 'which means you are underweight.')

        elif bmi > 18.5 and bmi <= 25:
            print('Your BMI is', bmi, 'which means you are normal.')

        elif bmi > 25 and bmi <= 30:
            print('your BMI is', bmi, 'overweight.')

        elif bmi > 30:
            print('Your BMI is', bmi, 'which means you are obese.')

        else:
            print('There is an error with your input')
            print('Please check you have entered whole numbers\n'
                  'and decimals were asked.')

        json_normalize(result['-L8DYqwcNQux9XjLg8ws'])
        print(result)
        return result

def feet2m(f, i):
    print(f,i)
    return (f*30.48 + i*2.54) * 0.01

def pound2kg(p):
    kg = p / 2.2
    return kg