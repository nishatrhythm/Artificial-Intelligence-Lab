# Neural Networks Lab
- A simple neural network with one output neuron, four inputs and weights, and bias.
- Design the previous example of a neural network by adjusting weights and biases randomly.
- A fully connected neural network — every neuron in the current layer has connections to every neuron from the previous layer.
- A fully connected neural network — every neuron in the current layer has connections to every neuron from the previous layer. You have 4 input neurons, one hidden layer consisting of 3 neurons, and one output neuron. You should adjust weights and biases randomly.
- Use a loop option to get the weights, inputs, and biases then fit into the neurons.
- Use the numpy library to calculate the dot product in the neural network.
- Use the numpy library to calculate the dot product in the neural network (Array).
- Take inputs containing 3 samples with 4 features and 3 neurons with weights and biases, respectively. Then print the outputs of the neurons.
- Use an input batch with weights and then transpose them to calculate the dot product.
- Two hidden layers with four neurons in the first layer and three in the second.
- Two hidden layers with four neurons in the first layer and three in the second with randomized weights and biases.
- Sigmoidal activation function.
- The Rectified Linear Unit (ReLU) activation function.
- Step function.
- Solve the 2-input AND gate problem using a neural network.
- Design the previous example of the neural network by adjusting weights and biases randomly.
- Solve the 3-input AND gate problem using a neural network.
- Solve the 2-input OR gate problem using a neural network.
- Design the previous example of the neural network by adjusting weights and biases randomly.
- Solve the 3-input OR gate problem using a neural network.
- Solve the NOT gate problem using a neural network.
- Design the previous example of the neural network by adjusting weights and biases randomly.
- **Code 18** - Design a neural network that has four input neurons, two hidden layers, and one output layer neuron. The activation function in the output payer should be sigmoidal. You should also adjust the weights and biases randomly. Moreover, the input dataset should contain 10 samples. Follow the figure:<br><br><img src="images/image1.png" alt="Image 1" width="600">
- **[Code 19](https://github.com/nishatrhythm/Neural-Networks/blob/main/code9.py)** - _[See below](https://github.com/nishatrhythm/Neural-Networks?tab=readme-ov-file#code-19)_
- **[Code 20](https://github.com/nishatrhythm/Neural-Networks/blob/main/code20.py)** - Solve OR gate using backpropagation.
- **[Code 21](https://github.com/nishatrhythm/Neural-Networks/blob/main/code21.py)** - Solve XOR gate using backpropagation.
- **[Code 22](https://github.com/nishatrhythm/Neural-Networks/blob/main/linearRegression.py)** - Predicting Salary Based on Years of Experience using Linear Regression.

# Code 19
Create a dataset using pandas for the following attributes and then predict the housing prices using neural network:
- Area: The total area of the house in square feet
- Bedrooms: The number of bedrooms in the house
- Bathrooms: The number of bathrooms in the house
- Age: The age of the house in years
- Location: The neighborhood or area where the house is located
- Garage Size: The size of the garage in square feet
- Yard Size: The size of the yard or outdoor space in square feet
- Amenities: A binary feature indicating whether the house has additional amenities such as a swimming pool, gym, etc
- School Rating: The rating of nearby schools, on a scale from 1 to 10
- Distance to City Center: The distance of the house from the city center in miles
- Price: The selling price of the house

## Dataset Example:
```
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
