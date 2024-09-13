import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Step 1: Create the Dataset
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

# Step 2: Preprocess the Data
X = df.drop('Price', axis=1)
y = df['Price']

# Apply one-hot encoding to 'Location' and scale the numerical features
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['Area', 'Bedrooms', 'Bathrooms', 'Age', 'Garage_Size', 'Yard_Size', 'Amenities', 'School_Rating', 'Distance_to_City_Center']),
        ('cat', OneHotEncoder(), ['Location'])
    ])

X_preprocessed = preprocessor.fit_transform(X)

# Step 3: Build and Train the Neural Network
X_train, X_test, y_train, y_test = train_test_split(X_preprocessed, y, test_size=0.2, random_state=42)

model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')

model.fit(X_train, y_train, epochs=100, validation_split=0.2, verbose=1)

# Evaluate the model
loss = model.evaluate(X_test, y_test)
print(f"Test loss: {loss}")

# Predicting the prices for the test set
predictions = model.predict(X_test)
print(f"Predicted prices: {predictions.flatten()}")