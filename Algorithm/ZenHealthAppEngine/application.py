from flask import Flask, json, Response, request
import numpy as np
import resources.datamanager as datamanager
import random


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

    if bglevel in np.arange(2.5, 5.9,0.1):
        print("this is normal range before meal..high cal meal")
        category = "High"
    if bglevel in np.arange(6.0 , 9.0, 0.1):
        print(" eat with less calories..medium")
        isLowCateloryDiet = True
        category = "Medium"
    if bglevel > 10.0:
        print('compulsory low caleroies')
        category = "Low"


    foodlist = datamanager.food_db.get('/foodData', None, params={'Course': 'Lunch'})
    print(len(foodlist))
    print(foodlist)
    new_fdata = {k: v for k, v in foodlist.items() if v['sugarLevel'] == category}
    print(len(new_fdata))
    for f_id, f_info in foodlist.items():
        # for key in f_info:
        #     print(key + ':', f_info[key])
        # print(f_info)

        if 'Course' in f_info:
            if 'Non Vegeterian'.lower() == f_info['allowedDiet'].lower():
                if timeslot in range(1, 12):
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

    if len(dinner) > 1:
        result['Dinner'] = random.sample(dinner, 5)
    elif len(dinner) < 5:
        result['Breakfast'] = dinner

    print(result)
    return result


if __name__ == "__main__":
    print("running on 0.0.0.0")
    app.run(debug=True)