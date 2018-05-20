import json
import requests
import os
from pprint import pprint
import pymongo
#from pymongo import MongoClient

def getRecipeData():
    #filePath = "C:\\Users\\cmalik\\Documents\\university\\cmpe295\\295b\\document.json"
    filePath = (os.path.join(os.getcwd(),"result.json"))
    if os.path.isfile(filePath):
        os.remove(filePath)
    recipeUrlList = ['http://api.yummly.com/v1/api/recipe/French-Onion-Soup-1332461?_app_id=dummyid&_app_key=dummykey']
    ''',
    'http://api.yummly.com/v1/api/recipe/Crock-Pot-Honey-Garlic-Chicken-1290814?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Weight-Loss-Wonder-Soup-2088497?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Healthy-Baked-Sweet-Potato-Fries-2221198?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Skinny-Mocha-Fudge-824977?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Coconut-Curry-Red-Lentil-Soup-2075988?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Healthy-Green-Smoothie-1031235?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Southwest-Hummus-Wraps-2171837?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Slow-Cooker-Chicken-and-Dumplings-2315303?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Rainbow-Carrot-Blossoms-With-Garlic-and-Herbs-2352554?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Easy-Oven-Roasted-Potatoes---A-simple-side-dish-to-love-2241306?_app_id=dummyid&_app_key=dummykey'
    ]
    '''
    
    for url in recipeUrlList:
        r = requests.get(url)
        data = r.json()
        extractDataFromUrl(filePath, data)
    
    
    

def extractDataFromUrl(filePath, data):
    recipeData = {}
    nutritionData = {}
    
    recipeData['Ingredients'] = data.get('ingredientLines')
    attrs = data.get('attributes')
    if attrs:
        recipeData['Course'] = attrs.get('course')
        recipeData['Cuisine'] = attrs.get('cuisine')
    recipeData ['Name'] = data.get('name')

    for nutrition in data['nutritionEstimates']:
        if nutrition['attribute'] == "ENERC_KCAL":
            nutritionData['Calories'] = str(nutrition['value']) + " " + nutrition['unit']['pluralAbbreviation']
        if nutrition['attribute'] == "SUGAR":
            nutritionData['Sugar'] = str(nutrition['value']) + " " + nutrition['unit']['pluralAbbreviation']
        if nutrition['attribute'] == "CHOCDF":
            nutritionData['Carbohydrates'] = str(nutrition['value']) + " " + nutrition['unit']['pluralAbbreviation']
    recipeData['Nutrients'] = nutritionData
    
    

    '''
    with open(filePath, 'a') as f:
        #f.write('')
        f.write(json.dumps(recipeData))
        f.write('\n \n')
        #f.write('\n')
    '''
    record.insert(recipeData)
    

#client = MongoClient('mongodb://localhost:27017/')
#print (client)

#db = client['FoodData']
#collection = db['FoodItems']

connection = pymongo.MongoClient("mongodb://localhost")
db=connection.FoodData
record = db.FoodItems
getRecipeData()



'''
'''
