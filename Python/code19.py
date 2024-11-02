import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

# Creating the dataset
data = {
    'Area': [2000, 1800, 2500, 2200, 1900, 2800, 2100, 1700, 2400, 2000],
    'Bedrooms': [3, 2, 4, 3, 2, 5, 4, 2, 3, 3],
    'Bathrooms': [2, 1.5, 3, 2.5, 2, 3.5, 2.5, 1, 3, 2],
    'Age': [10, 5, 15, 8, 3, 20, 12, 6, 18, 9],
    'Location': ['Suburban', 'Urban', 'Rural', 'Suburban', 'Urban', 'Rural', 'Suburban', 'Urban', 'Rural', 'Suburban'],
    'Garage_Size': [400, 300, 500, 450, 350, 600, 400, 250, 550, 400],
    'Yard_Size': [800, 600, 1000, 900, 700, 1200, 800, 500, 1100, 800],
    'Amenities': [1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    'School_Rating': [8, 7, 6, 9, 8, 5, 7, 6, 4, 8],
    'Distance_to_City_Center': [5, 2, 10, 7, 4, 15, 6, 3, 12, 5],
    'Price': [300000, 250000, 350000, 320000, 280000, 400000, 310000, 240000, 370000, 300000]
}

df = pd.DataFrame(data)

# Convert categorical variable 'Location' into dummy/indicator variables
df = pd.get_dummies(df, columns=['Location'], drop_first=True)

# Splitting the dataset into features and target
X = df.drop('Price', axis=1)
y = df['Price']

# Splitting the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardizing features by removing the mean and scaling to unit variance
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Training the neural network model
model = MLPRegressor(hidden_layer_sizes=(100, 100), activation='relu', solver='adam', max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train)

# Predicting on the test set
y_pred = model.predict(X_test_scaled)

# Calculating mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)