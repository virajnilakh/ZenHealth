from sklearn.externals import joblib
import numpy as np
import pandas as pd
#import resources.datamanager as datamanager
from resources.connection import UserProfile
from resources.connection import FoodConsumed
from pandas.io.json import json_normalize
import random
import json

class Service():

    def load_models(self):
        global USER_CLASSIFIER_MODEL
        global RECOMMENDER_MODEL

        USER_CLASSIFIER_MODEL = joblib.load('models/user_classifier.pkl')
        RECOMMENDER_MODEL = joblib.load('models/item_similarity.pkl')

    def test(self, userid, timeslot, bglevel, sugarConsumed):
        print("test recommednations")


    def feet2m(f, i):
        print(f,i)
        return (f*30.48 + i*2.54) * 0.01

    def pound2kg(self,p):
        kg = p / 2.2
        return kg



    def getBMI(self,height,weight):
        m =height * 30.48 * 0.01
        #print(m)
        kg = self.pound2kg(weight)
        #print(kg)

        bmi = round(kg / (m * m))
        print("Your body mass index is: ", bmi)
        return bmi


    def getUserDF(self,user, timeslot, bglevel, sugarConsumed):

        print("user for which recommendaations are provided:", user)
        name = user.uname
        gender = user.gender
        if(gender == 'male'):
            df_enc = 1
        else:
            df_enc = 0

        bmi = self.getBMI( user.height,int(user.weight))
        df = pd.DataFrame.from_dict(json_normalize({'bloodglucodelevel': bglevel, 'bmi': bmi,
                                                    'sugarcomsumed': sugarConsumed, 'gender': df_enc,
                                                    'label': 0}), orient='columns')

        return df

    def getUserCategory(self,user, timeslot, bglevel, sugarConsumed):

        #best_model = joblib.load('models/user_classifier.pkl')

        df = self.getUserDF(user, timeslot, bglevel, sugarConsumed)
        predicted_category = USER_CLASSIFIER_MODEL.predict(df)

        return predicted_category[0]

    def getResults(self,uname, timeslot, bglevel, sugarConsumed):

        #get user from mysql
        print("input uname is ",uname)
        u1 = UserProfile.query.get(uname)
        user = UserProfile.query.filter_by(uname=uname).first()
        if user is None:
            user = UserProfile('arpita@gmail.com')
            user.diet = 'Pescetarian'
            user.gender ='male'
            user.allergies = 'Dairy-Free'
            user.name = 'arpita'
            user.weight = 57
            user.height = 5.4
        print("user for which analysis :" , user)
        user_cat = self.getUserCategory(user, timeslot, bglevel, sugarConsumed)
        print("user category found is:", user_cat)

        #if user's history is not present in the database go to coldstart

        # foodlist = datamanager.food_db.get('/foodData', None)
        with open('dataset/fooditem.json') as json_data:
            foodlist = json.load(json_data)
        print("food data size found:" ,len(foodlist))
        #print(foodlist)
        output = {}
        consumed_food = []
        foodconsumed = FoodConsumed.query.filter_by(uname=uname).all()
        cnt =0
        if len(foodconsumed) == 0:
            isColdStart = True
        else:
            isColdStart = False
            for row in foodconsumed:
                print(row.fooditem)

                cnt =cnt+1
                consumed_food.append(row.fooditem)
                if cnt == 5:
                    break


        if isColdStart == True:
            output = self.coldstart(foodlist,timeslot,"John",user_cat,"Non Vegeterian")
        else:
            output = self.personalizedRecom(foodlist,consumed_food,timeslot)
        return output

    def createFoodDF(self, user_cat , foodlist):
        filtered_data = pd.DataFrame()
        food_result = []
        for key, value in foodlist.items():
              food_result.append(value)
        df = pd.DataFrame.from_dict(json_normalize(food_result), orient='columns')
        df = df.columns = ['fooditem', 'Course', 'Cuisine', 'Ingredients', 'Name', 'Nutrients.Calories',
                           'Nutrients.Carbohydrates', 'Nutrients.Sugar'
            , 'allowedAllergy', 'allowedDiet', 'allowedIngredient', 'sugarLevel']
        #  #print(df)
        diet = 'Non Vegeterian'
        allowedAllergy = 'Dairy-Free'
        print(df)
        if user_cat == 1:
            filtered_data = df.loc[df['sugarLevel'] == 'Low']
        elif user_cat == 2:
            filtered_data = df.loc[df['sugarLevel'] == 'Medium']
        elif user_cat == 3:
            filtered_data = df.loc[df['sugarLevel'] == 'High']

        filtered_data = df.loc[df['allowedDiet'] == diet]
        filtered_data = df.loc[df['allowedAllergy'] == allowedAllergy]

        print("final length:", filtered_data.shape)

        # new_fdata.to_json(result, orient='records', lines=True)
        out = filtered_data.to_json(orient='records')[1:-1].replace('},{', '} {')
        return out

    def personalizedRecom(self, foodlist, already_consumed_fooditems, timeslot):

        lunchCnt = 0
        bfCnt =0
        dinnerCnt =0
        lunch = []
        bf = []
        dinner = []
        result = {}
        df = pd.read_csv('dataset/encoded_fooditem.csv')
        #model = joblib.load('models/item_similarity.pkl')

        already_consumed_fooditems = ['INDIAN CHOLE', 'Grilled Marinated Flank Steak']
        rec = []
        for item in already_consumed_fooditems:
            row = df.loc[df['Name'] == item]
            # print(row)
            match = []
            match.append(row['fooditem'].values[0])
            match.append(row['e_infredients'].values[0])
            match.append(row['e_Name'].values[0])
            match.append(row['e_Nutrients.Calories'].values[0])
            match.append(row['e_Nutrients.Carbohydrates'].values[0])
            match.append(row['e_Nutrients.Sugar'].values[0])
            match.append(row['e_sugarLevel'].values[0])
            # print(match)
            # fooditem e_infredients e_Name e_Nutrients.Calories e_Nutrients.Carbohydrates e_Nutrients.Sugar e_sugarLevel
            u, i =RECOMMENDER_MODEL.kneighbors([match])
            rec = rec + list(i[0])
            print(list(i[0]))
            print('**********')

        print(rec)
        for k in rec:
            row = df.loc[df['e_Name'] == k]
            print(row)
            if 'Nutrients.Sugar' in row:
                print(row['Name'].values[0], " : ", row['Nutrients.Sugar'].values[0].astype(str))
                if timeslot in range(1, 12):
                    if 'Lunch' in row['Course'].values[0]:
                        lunch.append(row['Name'].values[0] +" : "+  row['Nutrients.Sugar'].values[0].astype(str))

                        lunchCnt += 1
                    if 'Breakfast and Brunch' in row['Course'].values[0]:
                        bf.append(row['Name'].values[0] +" : "+  row['Nutrients.Sugar'].values[0].astype(str))
                        bfCnt += 1
                    if 'Main Dishes' in row['Course'].values[0]:
                        dinner.append(row['Name'].values[0] +" : "+  row['Nutrients.Sugar'].values[0].astype(str))
                        dinnerCnt += 1

                elif timeslot in range(13, 16):
                    if 'Lunch' in row['Course'].values[0]:
                        lunch.append(row['Name'].values[0] +" : "+  row['Nutrients.Sugar'].values[0].astype(str))
                        lunchCnt += 1
                    if 'Main Dishes' in row['Course'].values[0]:
                        dinner.append(row['Name'].values[0] +" : "+  row['Nutrients.Sugar'].values[0].astype(str))
                        dinnerCnt += 1


                elif timeslot in range(17, 23):
                    if 'Main Dishes' in row['Course'].values[0]:
                        dinner.append(row['Name'].values[0] +" : "+  row['Nutrients.Sugar'].values[0].astype(str))
                        dinnerCnt += 1

        print(len(lunch), len(bf), len(dinner))
        if len(lunch) > 5:
            result['Lunch'] = random.sample(lunch, 5)
        elif len(lunch) < 5:
            result['Lunch'] = lunch

        if len(bf) < 5:
            result['Breakfast'] = bf
        elif len(bf) > 5:
            result['Breakfast'] = random.sample(bf, 5)

        if len(dinner) > 5:
            result['Dinner'] = random.sample(dinner, 5)
        elif len(dinner) < 5:
            result['Breakfast'] = dinner

        print(result)
        return result

    def coldstart(self,foodlist,timeslot, user, category, diet):
        result = {}
        bf = []
        bfCnt = 0
        lunch = []
        lunchCnt = 0
        dinner = []
        dinnerCnt = 0
        if category == 1:
            level = "Low"
        elif category == 2:
            level = "Medium"
        elif category == 3:
            level = "High"

        for f_id, f_info in foodlist.items():
            print(f_info)
            if 'Nutrients'in f_info:
                if 'Course' in f_info:
                    if diet.lower() == f_info['allowedDiet'].lower():
                        if level.lower() == f_info['sugarLevel'].lower():
                            if timeslot in range(1, 12):
                                if 'Lunch' in f_info['Course']:
                                    lunch.append(f_info['Name']  +" : "+ f_info['Nutrients']['Sugar'].replace("grams" ,""))

                                    lunchCnt += 1
                                if 'Breakfast and Brunch' in f_info['Course']:
                                    bf.append(f_info['Name'] +" : "+ f_info['Nutrients']['Sugar'].replace("grams" ,""))
                                    bfCnt += 1
                                if 'Main Dishes' in f_info['Course']:

                                    dinner.append(f_info['Name'] +" : "+ f_info['Nutrients']['Sugar'].replace("grams" ,""))
                                    dinnerCnt += 1

                            elif timeslot in range(13, 16):
                                if 'Lunch' in f_info['Course']:
                                    lunch.append(f_info['Name'] +" : "+ f_info['Nutrients']['Sugar'].replace("grams" ,""))
                                    lunchCnt += 1
                                if 'Main Dishes' in f_info['Course']:
                                    dinner.append(f_info['Name'] +" : "+ f_info['Nutrients']['Sugar'].replace("grams" ,""))
                                    dinnerCnt += 1


                            elif timeslot in range(17, 23):
                                if 'Main Dishes' in f_info['Course']:
                                    dinner.append(f_info['Name'] +" : "+ f_info['Nutrients']['Sugar'].replace("grams" ,""))
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
        return  result



