import numpy as np

inputs = np.array([[0, 0],
                   [0, 1],
                   [1, 0],
                   [1, 1]])

labels = np.array([0, 1, 1, 1]) 

# Define the weights and bias for the neural network
weights = np.array([0.5, 0.5]) 
bias = -0.2 

# Define the activation function (step function)
def step_function(x):
    return 0 if x <= 0 else 1

# Perform the forward pass to compute the outputs
outputs = []
for input_row in inputs:
    weighted_sum = np.dot(input_row, weights) + bias
    output = step_function(weighted_sum)
    outputs.append(output)

# Compare the predicted outputs with the actual labels
correct_predictions = np.sum(outputs == labels)

# Print the results
print("Inputs:", inputs)
print("Labels:", labels)
print("Predicted Outputs:", outputs)
print("Correct Predictions:", correct_predictions)