import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics
import pickle


data = pd.read_csv("C:/Users/abhij/Desktop/Minor Mini Project/calories_data")
data.replace({"Gender":{'male':0,'female':1}}, inplace=True)
X = data.drop(columns=['User_ID','Calories'], axis=1)
Y = data['Calories']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
Y = data['Calories']
model = XGBRegressor()


model.fit(X_train, Y_train)



pickle.dump(model, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))


