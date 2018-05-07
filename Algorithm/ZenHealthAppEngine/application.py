from flask import Flask, json, Response, request
import numpy as np
import pandas as pd
import random
from sklearn.externals import joblib
from pandas.io.json import json_normalize


app = Flask(__name__)
app.debug = True


@app.route("/v1/zenloop/ping", methods=['GET'])
def testPing():
    print("ping successfull")
    return json.dumps({'status': 'ok', 'message': 'Zenhealth API service :v1'})

@app.route("/v1/zenloop/foodRecommendations", methods=['GET'])
def getFoodRecommendations():

    args = request.args
    print(args)  # For debugging
    userid = args['userid']
    timeslot = int(args['timeslot'])
    bglevel = float(args['bglevel'])
    sugarConsumed = float(args['sugarConsumed'])
    recommendations = getData(userid, timeslot, bglevel, sugarConsumed)
    resp = Response(json.dumps(recommendations))
        # resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'app/json'
    return resp

def check(value):
    if 0.50 <= value <= 150 and round(value,2)==value:
        return True

def getData(userid, timeslot, bglevel, sugarConsumed):
    print("retriving data");

    category = None
    result = {}
    new_fdata = None
    bf = []
    bfCnt = 0
    lunch = []
    lunchCnt = 0
    dinner = []
    dinnerCnt = 0

    best_model = joblib.load('dataset/user_classifier.pkl')
    df = pd.DataFrame.from_dict(json_normalize({'id': 23, 'bloodglucodelevel': bglevel, 'bmi': 7.4,
                                                'sugarcomsumed': sugarConsumed, 'gender': gender, 'user': name,
                                                'label': 0}), orient='columns')

    predicted_category = best_model.predict(df)
    print(predicted_category)
    print(category)
    foodlist = pd.read_csv('dataset/fooditem.csv')
    print(len(foodlist))

    # if sugarConsumed > 11:
    #     new_fdata = foodlist.loc[foodlist['sugarLevel'] == 'Low']
    # elif 7.0 <=sugarConsumed <= 11:
    #     new_fdata = foodlist.loc[foodlist['sugarLevel'] == 'Medium']
    # elif 0.0 <= sugarConsumed <7 :
    #     new_fdata = foodlist.loc[foodlist['sugarLevel'] == 'High']
    #
    # print(len(new_fdata))

    if 5.0 <= bglevel <= 7.2:
        print("this is normal range before meal..high cal meal")
        new_fdata = foodlist.loc[foodlist['sugarLevel'] == 'High']
    if 7.2 < bglevel <= 9.9:
        print(" eat with less calories..medium")
        isLowCateloryDiet = True
        new_fdata = foodlist.loc[foodlist['sugarLevel'] == 'Medium']
    if bglevel > 10.0:
        print('compulsory low caleroies')
        new_fdata = foodlist.loc[foodlist['sugarLevel'] == 'Low']
    print(len(new_fdata))

    #new_fdata = foodlist.loc[foodlist['allowedDiet'] == 'Non Vegeterian']

    print(len(new_fdata))

    for f_id, f_info in new_fdata.iterrows():
        # for key in f_info:
        #     print(key + ':', f_info[key])
        course = []
        #print(f_info['Course'])
        course = str(f_info['Course'])
        if f_info['Course'] != None:
            if timeslot in range(1, 12):
                    if course.find('Lunch'):
                        lunch.append(f_info['Name'])
                        lunchCnt += 1
                    if 'Breakfast and Brunch' in course:
                        bf.append(f_info['Name'])
                        bfCnt += 1
                    if 'Main Dishes' in course:
                        dinner.append(f_info['Name'])
                        dinnerCnt += 1

            elif timeslot in range(13, 16):
                    if 'Lunch' in course:
                        lunch.append(f_info['Name'])
                        lunchCnt += 1
                    if 'Main Dishes' in course:
                        dinner.append(f_info['Name'])
                        dinnerCnt += 1


            elif timeslot in range(17, 23):
                    if 'Main Dishes' in course:
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

    if len(dinner) > 1:
        result['Dinner'] = random.sample(dinner, 5)
    elif len(dinner) < 5:
        result['Breakfast'] = dinner

    print(result)
    return result


if __name__ == "__main__":
    print("running on 0.0.0.0")
    app.run(debug=True)