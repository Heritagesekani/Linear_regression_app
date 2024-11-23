import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import joblib

#import dataset
df=pd.read_excel("data/data.xlsx")

#independent dependent features
x=df.iloc[:, :-1].values
y=df.iloc[:, -1].values

# creating the training set and test set
x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2, random_state=42)

#Building and training the model
model = LinearRegression()

# Train the model
model.fit(x_train, y_train)

#inferece
y_pred = model.predict(x_test)
print(y_pred)

#making the prediction a single data point with AT=15,V=40, AP=1000, RH=75
model.predict([[15,40,1000,75]])

#EVALUATING THE MODEL
#R_squared
r2 = r2_score(y_test, y_pred)
print(r2)

#Adjusted R-squared
k= x_test.shape[1]
n= x_test.shape[0]
adj_r2 = 1-(1-r2)*(n-1)/(n-k-1)
print(adj_r2)
#scatter plot of actual vs. predicted
#Save the train model to a .pkl file
plt.scatter(y_test, y_pred, color='blue')  # Scatter plot for actual vs predicted
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red')  # Plot the line
plt.xlabel('Actual values')
plt.ylabel('Predicted values')
plt.title('Linear Regression Results')
plt.show()

#save the trained model to a .pkl file
joblib.dump(model, "model/model.pkl")