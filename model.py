import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import warnings
warnings.filterwarnings('ignore')
import pickle

data=pd.read_csv('dataset.csv')
dataset=data[['Year','Selling_Price','Present_Price','Kms_Driven','Fuel_Type','Seller_Type','Transmission','Owner']]
dataset['Present_Year']=2022
dataset['Number_of_Years_Old']=dataset['Present_Year']- dataset['Year']
dataset.drop(labels=['Year', 'Present_Year'],axis=1,inplace=True)
Fuel_Type=dataset[['Fuel_Type']]
Fuel_Type=pd.get_dummies(Fuel_Type, drop_first=True)

Seller_Type=dataset[['Seller_Type']]
Seller_Type=pd.get_dummies(Seller_Type, drop_first=True)

Transmission=dataset[['Transmission']]
Transmission=pd.get_dummies(Transmission, drop_first=True)

dataset=pd.concat([dataset,Fuel_Type, Seller_Type, Transmission], axis=1)

dataset.drop(labels=['Fuel_Type', 'Seller_Type', 'Transmission'], axis=1, inplace=True)

sell=dataset['Selling_Price']
dataset.drop(['Selling_Price'], axis=1, inplace=True)
dataset=dataset.join(sell)

X=dataset.iloc[:,:-1]
y=dataset.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

model = DecisionTreeRegressor(random_state = 1)
model.fit(X_train, y_train)
y_pred=model.predict(X_test)
d=model.predict([[10.85, 7980, 1, 2, 1, 1, 0, 1]])
print(d)


pickle.dump(model, open("dtrmodel.pkl", "wb"))

# load model from file
model = pickle.load(open("dtrmodel.pkl", "rb"))

