
# coding: utf-8

# In[11]:

#Import Library


import pandas as pd

from sklearn import preprocessing


# In[25]:

# ------------------------------- similarity approach------------------------------

food_df = pd.read_csv('../dataset/fooditem.csv')
food_df.columns = ['fooditem' , 'Course','Cuisine','Ingredients' , 'Name' , 'Nutrients.Calories' , 
                      'Nutrients.Carbohydrates','Nutrients.Sugar' 
                   ,'allowedAllergy','allowedDiet','allowedIngredient','sugarLevel']
food_df.head(3)


# In[26]:
data = pd.DataFrame()
data['Course'] = food_df['Course']
to_drop = ['Course','Cuisine' , 'allowedAllergy' , 'allowedDiet', 'allowedIngredient'
          ]
food_df.drop(to_drop, inplace=True, axis=1)

food_df.head(3)


# In[27]:

import re
def clean_df(column):
    column = re.sub(r'([^\.\s\w]|_)+', '', column).replace(".", ". ")    
    return column

def clean_units(column):
    column = column.replace("grams","")
    column = column.replace("kcal","")
    return column


# In[28]:


food_df['Ingredients'] = food_df['Ingredients'].map(lambda j: clean_df(j))
food_df['Name'] = food_df['Name'].map(lambda j: clean_df(j))
food_df['Nutrients.Calories'] = food_df['Nutrients.Calories'].map(lambda j: clean_units(str(j)))
food_df['Nutrients.Carbohydrates'] = food_df['Nutrients.Carbohydrates'].map(lambda j: clean_units(str(j)))
food_df['Nutrients.Sugar'] = food_df['Nutrients.Sugar'].map(lambda j: clean_units(str(j)))
food_df.head(3)


# In[29]:

le = preprocessing.LabelEncoder()
df_encoded = food_df.apply(le.fit_transform)
df_encoded.columns = ['fooditem' , 'e_infredients' , 'e_Name' , 'e_Nutrients.Calories' , 
                      'e_Nutrients.Carbohydrates','e_Nutrients.Sugar' ,'e_sugarLevel']
df_encoded.shape
df_encoded.head(3)


# In[30]:

df = pd.merge(food_df, df_encoded, on ='fooditem')
df['Course'] = data['Course']
df.head(3)
df.to_csv('../dataset/encoded_fooditem.csv', sep=',' ,  index = False)

# In[8]:

# *************** cosine similarity *********************

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity  

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(df_encoded)
#print(tfidf_matrix)
cosine = cosine_similarity(df_encoded[0:1], df_encoded)
#print(cosine)
cosine.sort()
print(cosine[0][-5:])


# In[9]:

#************************* neighbourhood similarity *********************

import numpy as np
from sklearn.neighbors import NearestNeighbors



# Next we will instantiate a nearest neighbor object, and call it nbrs. Then we will fit it to dataset X.
model = NearestNeighbors(n_neighbors=10, algorithm='ball_tree').fit(df_encoded)

# Let's find the k-neighbors of each point in object X. To do that we call the kneighbors() function on object X.
distances, indices = model.kneighbors(df_encoded)

# Let's print out the indices of neighbors for each record in object X.
indices


# In[112]:

#sample
# u, i = nbrs.kneighbors([[2,
# 370,
# 216,
# 370,
# 458,
# 216,
# 0]])
     
# print(i)
already_consumed_fooditems = [ 'INDIAN CHOLE', 'Grilled Marinated Flank Steak']
result = []
for item in already_consumed_fooditems:
    row = df.loc[df['Name'] == item]
    #print(row)
    match = []
    match.append(row['fooditem'].values[0])
    match.append( row['e_infredients'].values[0])
    match.append( row['e_Name'].values[0])
    match.append( row['e_Nutrients.Calories'].values[0])
    match.append( row['e_Nutrients.Carbohydrates'].values[0])
    match.append( row['e_Nutrients.Sugar'].values[0])
    match.append( row['e_sugarLevel'].values[0])
    #print(match)
    #fooditem e_infredients e_Name e_Nutrients.Calories e_Nutrients.Carbohydrates e_Nutrients.Sugar e_sugarLevel
    u, i =model.kneighbors([ match ])
    result = result + list(i[0])
    print(list(i[0]))
    print('**********')

print(result)


# In[113]:

for k in result:
    
    row = df.loc[df['e_Name'] == k]
    print(row['Name'].values[0] ," : ",  row['Nutrients.Sugar'].values[0])


# In[114]:

from sklearn.externals import joblib
joblib.dump(model, 'item_similarity.pkl')


# In[115]:

# test model
test_model = joblib.load('item_similarity.pkl')


# In[116]:

user_food_df = pd.read_csv('../dataset/user_fooditem.csv')
user_food_df.head()

test = pd.merge(user_food_df, food_df, on='fooditem')
test.head(3)
#test.shape


# In[117]:

users = {}

distinct_users=np.unique(user_food_df['userid'])
for user in distinct_users:
    data =test[test['userid'] == user]['Name'].values
    #print(data)
    if user in users:
        users[user].append(data[0])
    else:
        users[user] = list(data)
     #already_consumed_fooditems.append(row[''])

print(users)


# In[137]:


rec = {}
for user, already_consumed_fooditems in users.items():
    result = []
    
    for item in already_consumed_fooditems:
        
        row = df.loc[df['Name'] == item]
        #print(row)
        match = []
        match.append(row['fooditem'].values[0])
        match.append( row['e_infredients'].values[0])
        match.append( row['e_Name'].values[0])
        match.append( row['e_Nutrients.Calories'].values[0])
        match.append( row['e_Nutrients.Carbohydrates'].values[0])
        match.append( row['e_Nutrients.Sugar'].values[0])
        match.append( row['e_sugarLevel'].values[0])
        #print(match)
        #fooditem e_infredients e_Name e_Nutrients.Calories e_Nutrients.Carbohydrates e_Nutrients.Sugar e_sugarLevel
        u, i =model.kneighbors([ match ])
        result = result + list(i[0])
        print(list(i[0]))
        print('**********')

            
    rec[user] = result

print(rec)


# In[139]:




# In[ ]:

names = []
for user,result in rec.items():
    for k in result:           
        row = df.loc[df['e_Name'] == k]
        print(row)
        name = print(row['Name'].values[0] ," : ",  row['Nutrients.Sugar'].values[0])
        names.append(name)

