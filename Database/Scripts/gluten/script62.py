from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 62
http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=393^Gluten-Free
&allowedDiet[]=388^Lacto%20vegetarian&allowedCourse[]=course^course-Main%20Dishes&maxResult=40&nutrition.SUGAR.min=1&nutrition.SUGAR.max=10

this script is for query 62, Main Dishes in course , sugar value is medium, allowed allergy: gluten, allowedDiet=Lacto vegetarian

'''                  
                     
def getRecipeData():
    recipeUrlList = [
                     'http://api.yummly.com/v1/api/recipe/Sweet-Potato-Avocado-Tacos-2141547?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Roasted-Chickpeas-with-Chipotle-and-Lime-_Vegan_-Gluten-Free_-1225168?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Creamy-Mushroom-and-Wild-Rice-Casserole-1119413?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Cheese-Enchiladas-1018019?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Crispy-Seasoned-Cauliflower-_Vegan_-1435409?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Chickpea-Tacos-1145721?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/One-Skillet-Mexican-Rice-Casserole-2000712?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Super-Quick-and-Easy-Mushroom-and-Tarragon-Stroganoff-1424092?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Slow-Cooker-Pumpkin_-Chickpea_-and-Red-Lentil-Curry-1322276?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Slow-Cooker-Burrito-Bowls-1552390?_app_id=dummyid&_app_key=dummykey'
                     ]
    
                     
    for url in recipeUrlList:
        r = requests.get(url)
        data = r.json()
        extractDataFromUrl(data)
        
def extractDataFromUrl(data):
    recipeData = {}
    nutritionData = {}
    
    recipeData['Ingredients'] = data.get('ingredientLines')
    attrs = data.get('attributes')
    if attrs:
        recipeData['Course'] = attrs.get('course')
        if (recipeData['Course'] == None):
            recipeData['Course'] = []
            recipeData['Course'].append("Main Dishes")
        recipeData['Cuisine'] = attrs.get('cuisine')
    else:
        recipeData['Course'] = "Main Dishes"
    recipeData ['Name'] = data.get('name')

    for nutrition in data['nutritionEstimates']:
        if nutrition['attribute'] == "ENERC_KCAL":
            if(nutrition['value'] is None):
                return
            nutritionData['Calories'] = str(nutrition['value']) + " " + nutrition['unit']['pluralAbbreviation']
        if nutrition['attribute'] == "SUGAR":
            if(nutrition['value'] is None):
                return
            nutritionData['Sugar'] = str(nutrition['value']) + " " + nutrition['unit']['pluralAbbreviation']
        if nutrition['attribute'] == "CHOCDF":
            if(nutrition['value'] is None):
                return
            nutritionData['Carbohydrates'] = str(nutrition['value']) + " " + nutrition['unit']['pluralAbbreviation']
    recipeData['Nutrients'] = nutritionData
    recipeData['allowedDiet'] = 'Lacto vegetarian'
    recipeData['allowedAllergy'] = 'Gluten-Free'
    recipeData['sugarLevel'] = 'Medium'
    #recipeData['allowedIngredient'] = 'bacon'
         
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

