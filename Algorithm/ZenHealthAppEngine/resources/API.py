import json

import numpy as np
import pandas as pd
import resources.datamanager as datamanager
import scipy as sp
from flask import Flask, render_template, request, session, flash, redirect, jsonify, json, Response
from pandas.io.json import json_normalize
from sklearn import preprocessing
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors.nearest_centroid import NearestCentroid
from pandas.io.json import json_normalize
import random
from sklearn.cluster import KMeans
# Algorithm
'''
connect to user profile  and get diet 
connect to db and get food details based on diet and time
'''
class API():

    def getFoodRecom(self,userid, timeslot, bglevel, sugarConsumed):
        print("fetching recommednations")

        #************************************ USER
        user = datamanager.user_db.get('/userProfile', userid)
        print(user)
        # The blood glucose target range for diabetics, according to the American Diabetes Association, should be 5.0–7.2 mmol / l (90–130 mg / dL) before meals,
        # and less than 10 mmol / L (180 mg / dL) after meals
        if bglevel in np.arange(5.0, 7.2, 0.1):
            print("this is normal range before meal")
        if bglevel > 7.2:
            print(" eat with less calories")
            isLowCateloryDiet = True

        diet = user.get('diet')
        m = user.get('height') * 30.48 * 0.01
        print(m)
        kg = pound2kg(int(user.get('weight')))
        print(kg)

        bmi = round(kg / (m * m))
        print("Your body mass index is: ", bmi)
        if bmi <= 18.5:
            print('Your BMI is', bmi, 'which means you are underweight.')

        elif bmi > 18.5 and bmi < 25:
            print('Your BMI is', bmi, 'which means you are normal.')

        elif bmi >= 25 and bmi <= 30:
            print('your BMI is', bmi, 'overweight.')
            isLowCateloryDiet = True

        elif bmi >= 30:
            print('Your BMI is', bmi, 'which means you are obese.')
            isLowCateloryDiet = True

        else:
            print('There is an error with your input')
            print('Please check you have entered whole numbers\n'
                  'and decimals were asked.')

        #******************************* Food recommendation for user
        result = {}
        bf = []
        bfCnt = 0
        lunch = []
        lunchCnt = 0
        dinner = []
        dinnerCnt = 0
        foodlist = datamanager.food_db.get('/foodData', None, params={'Course' : 'Lunch'})
        print(len(foodlist))
        print(foodlist)
        food_result = []
        for key, value in foodlist.items():
            food_result.append(value)

        print(food_result)
        df = pd.DataFrame.from_dict(json_normalize(food_result), orient='columns')
        print(df)
        df.shape
        df.to_csv("fooditem.csv", sep=',');

        #filter fooditems for low sugar
        if sugarConsumed > 11:
            new_fdata = {k: v for k, v in foodlist.items() if v['sugarLevel'] == 'Low'}
        elif sugarConsumed < 7:
            new_fdata = {k: v for k, v in foodlist.items() if v['sugarLevel'] == 'Medium'}
        else:
            new_fdata = {k: v for k, v in foodlist.items() if v['sugarLevel'] == 'High'}

        for f_id, f_info in new_fdata.items():
            # for key in f_info:
            #     print(key + ':', f_info[key])
            #print(f_info)

            if 'Course' in f_info:
                if 'Non Vegeterian'.lower() == f_info['allowedDiet'].lower():
                    if timeslot in range(4, 12):
                        if 'Lunch' in f_info['Course']:
                            lunch.append(f_info['Name'])
                            lunchCnt += 1
                        if 'Breakfast and Brunch' in f_info['Course']:
                            bf.append(f_info['Name'])
                            bfCnt += 1
                        if 'Main Dishes' in f_info['Course']:
                            dinner.append(f_info['Name'])
                            dinnerCnt += 1

                    elif timeslot in range(13, 16):
                        if 'Lunch' in f_info['Course']:
                            lunch.append(f_info['Name'])
                            lunchCnt += 1
                        if 'Main Dishes' in f_info['Course']:
                            dinner.append(f_info['Name'])
                            dinnerCnt += 1


                    elif timeslot in range(17, 23):
                        if 'Main Dishes' in f_info['Course']:
                            dinner.append(f_info['Name'])
                            dinnerCnt += 1




        print(len(lunch), len(bf), len(dinner))
        if len(lunch) > 1:
            result['Lunch'] = random.sample(lunch, 5)
        elif len(lunch) < 5:
            result['Lunch'] = lunch

        if len(bf) < 5:
            result['Breakfast'] = bf
        elif len(bf) > 1:
            result['Breakfast'] = random.sample(bf, 5)

        if len(dinner) > 1 :
            result['Dinner'] = random.sample(dinner, 5)
        elif len(dinner)  < 5:
            result['Breakfast'] = dinner

        print(result)

        return result

def feet2m(f, i):
    print(f,i)
    return (f*30.48 + i*2.54) * 0.01

def pound2kg(p):
    kg = p / 2.2
    return kg