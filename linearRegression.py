import pandas as pd
import numpy as np
import random
data = {
    "Year of Experiences": [3, 5, 2, 7, 4, 6, 1, 9, 8, 10, 2, 4, 6, 8, 5, 3, 7, 9, 4, 6],
    "Salary": [45000, 60000, 38000, 75000, 52000, 68000, 30000, 90000, 82000, 100000, 36000, 50000, 72000, 85000, 59000, 42000, 77000, 92000, 54000, 69000]
}
dataset = pd.DataFrame(data)
dataset

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

x = dataset[['Year of Experience']]
y = dataset['Salary']
model = LinearRegression()
model.fit(x, y)

experience= np.array([[11]])
salary = model.predict(experience)
print(salary)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
y_test = [109000]
y_pred = salary

mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error (MAE):", mae)

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error (MSE):", mse)

rmse = np.sqrt(mse)
print("Root Mean Squared Error (RMSE):", rmse)

r2 = r2_score(y_test, y_pred)
print("R2 Score:", r2)
