# OR gate using backpropagation

import numpy as np

# Activation function: Sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Input dataset for OR
inputs = np.array([[0, 0],
                   [0, 1],
                   [1, 0],
                   [1, 1]])

# Expected output for OR
outputs = np.array([[0],
                    [1],
                    [1],
                    [1]])

# Set seed for reproducibility
np.random.seed(42)

# Initialize weights and biases
input_layer_neurons = inputs.shape[1]
hidden_layer_neurons = 2
output_neurons = 1

# Weights and biases for the hidden layer
wh = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
bh = np.random.uniform(size=(1, hidden_layer_neurons))

# Weights and biases for the output layer
wo = np.random.uniform(size=(hidden_layer_neurons, output_neurons))
bo = np.random.uniform(size=(1, output_neurons))

# Learning rate
lr = 0.1

# Number of epochs
epochs = 10000

# Training the neural network
for epoch in range(epochs):
    # Forward Propagation
    hidden_layer_input = np.dot(inputs, wh) + bh
    hidden_layer_output = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_output, wo) + bo
    predicted_output = sigmoid(output_layer_input)

    # Calculate the error
    error = outputs - predicted_output

    # Backpropagation
    d_predicted_output = error * sigmoid_derivative(predicted_output)
    error_hidden_layer = d_predicted_output.dot(wo.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    # Update weights and biases
    wo += hidden_layer_output.T.dot(d_predicted_output) * lr
    bo += np.sum(d_predicted_output, axis=0, keepdims=True) * lr
    wh += inputs.T.dot(d_hidden_layer) * lr
    bh += np.sum(d_hidden_layer, axis=0, keepdims=True) * lr


    if (epoch + 1) % 1000 == 0:
        print(f'Epoch {epoch+1}, Error: {np.mean(np.abs(error))}')

print("Final predicted output for OR gate:")
print(predicted_output)