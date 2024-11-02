import numpy as np

# Define inputs (3 samples with 4 features each)
inputs = np.array([
    [1, 2, 3, 2.5],
    [2.0, 5.0, -1.0, 2.0],
    [-1.5, 2.7, 3.3, -0.8]
])

# Define weights (3 neurons with 4 weights each)
weights = np.array([
    [0.2, 0.8, -0.5, 1],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
])

# Define biases (3 biases, one for each neuron)
biases = np.array([2, 3, 0.5])

# Perform calculations
# np.dot() performs the dot product between inputs and weights, then add biases
outputs = np.dot(inputs, weights.T) + biases
print(outputs)