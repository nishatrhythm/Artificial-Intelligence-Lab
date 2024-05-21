import numpy as np

# Define the inputs and corresponding labels for the AND gate
inputs = np.array([[0, 0],
                   [0, 1],
                   [1, 0],
                   [1, 1]])

labels = np.array([0, 0, 0, 1])

# Define the range for random initialization
weight_range = (-1, 1)
bias_range = (-1, 1)

# Randomly initialize the weights and bias within the defined range
weights = np.random.uniform(low=weight_range[0], high=weight_range[1], size=(2,))
bias = np.random.uniform(low=bias_range[0], high=bias_range[1])

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