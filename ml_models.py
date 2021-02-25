# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
#importing the dataset
data=pd.read_csv('insurance.csv')

#encode the categorical data(region,sex,smoker)
data=pd.get_dummies(data,drop_first=True)

Y=data['charges']
print(Y)
data=data.drop(['charges'],axis=1)
X=data
print(X)

#splitting the dataset
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

# simple linear regression
#from sklearn.linear_model import LinearRegression
#regression=LinearRegression()
#regression.fit(x_train,y_train)
#y_pred=regression.predict([[19,0,27.9,0,1,3]])
#print(regression.score(x_test,y_test))


#decision tree regressor
#from sklearn.tree import DecisionTreeRegressor  
# create a regressor object 
#regressor = DecisionTreeRegressor(random_state = 0)  
#regressor.fit(x_train,y_train)
#print(regressor.score(x_test,y_test)) 

#here, random forest regressor gives the best score
from sklearn.ensemble import RandomForestRegressor 
regressor = RandomForestRegressor(n_estimators = 100, random_state = 0,max_depth=4) 
regressor.fit(x_train,y_train) 
print(regressor.score(x_test,y_test))
# save the model to disk
filename = 'model.sav'
pickle.dump(regressor, open(filename, 'wb'))


#load the model
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.predict([[19,27.9,0 ,0,1,0, 0,1]])
print(result)
