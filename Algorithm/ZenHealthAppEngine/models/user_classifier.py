
# coding: utf-8

# In[80]:

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


# In[81]:

data = pd.read_csv('../dataset/user_classifier.csv')
Y = data['label']
data.head()


# In[82]:

#preprocessing
X = pd.DataFrame()

X_dec = data['gender']
X_dec_user = data['user']

le = preprocessing.LabelEncoder()
X_enc = le.fit_transform(data['gender'])
print(X_enc)
X['gender'] = X_enc
X['bloodglucoselevel'] = data['bloodglucoselevel']
X['bmi'] = data['bmi']
X['sugarcomsumed'] = data['sugarcomsumed']
X['label'] = data['label']
#X['user'] = X_enc_user

X.head(3)


# In[83]:

print(X.shape)
print(Y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.30, random_state=99)

print("X_train total length:",len(X_train))
print("X_test total length:",len(X_test))
print("Y_train total length:",len(y_train))


# In[84]:

model_nb = GaussianNB()
model_svm = svm.SVC()
model_lr = LogisticRegression()
model_knn_centroid = NearestCentroid()
model_knn = KNeighborsClassifier()
eclf = VotingClassifier(estimators=[('lr', model_lr), ('knn_centroid', model_knn_centroid), ('gnb', model_nb), ('svc', model_svm), ('knn', model_knn)],
voting='hard', weights=[1,1,1,1,1])

models = [ model_nb, model_svm, model_lr, model_knn_centroid, model_knn, eclf]
model_names = [ "Naive Bayes", "SVM", "Logistic Regression", "Nearest Neighbors using Centroid", "K-nearest Neighbors", "Ensemble"]
    
best_model = None
best_accuracy = 0
best_preds = None


# In[85]:

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
print("Best model:",best_model)
print("Best accuracy:",best_accuracy)
print("Best predictions:",best_preds)  


# In[86]:

results = X_train
X_test = X_test.drop('label',1)
X_test['label'] = best_preds
results.append(X_test)
results.head()


# In[98]:


results = results.drop('gender',1)
#results = results.drop('user',1)

results['gender'] = X_dec
#results['user'] = X_dec_user

results.head()


# In[99]:

#predict for the new user 

from pandas.io.json import json_normalize
df = pd.DataFrame.from_dict(json_normalize({ 'bloodglucodelevel':180, 'bmi' :28 , 
                                            'sugarcomsumed' :10, 'gender':0,  'label': 0}), orient='columns')


predicted = best_model.predict(df)

print(predicted)


# In[94]:

import pickle
filename = 'user_classifier_model.sav'
pickle.dump(best_model, open(filename, 'wb'))


# In[95]:



from sklearn.externals import joblib
joblib.dump(best_model, 'user_classifier.pkl')


# In[96]:

best_model_pkl = joblib.load('user_classifier.pkl')

loaded_model = pickle.load(open(filename, 'rb'))
# In[97]:

predicted = loaded_model.predict(df)

print(predicted)


# In[ ]:




# In[ ]:



