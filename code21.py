# XOR gate using backpropagation

import numpy as np

input_neurons = 2
hidden_neurons = 2
output_neurons = 1

learning_rate = 0.1

np.random.seed(42)
weights_input_hidden = np.random.rand(input_neurons, hidden_neurons)
bias_hidden = np.random.rand(hidden_neurons)
weights_hidden_output = np.random.rand(hidden_neurons, output_neurons)
bias_output = np.random.rand(output_neurons)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)


inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs = np.array([[0], [1], [1], [0]])


epochs = 10000
for epoch in range(epochs):
    # Forward propagation
    hidden_layer_input = np.dot(inputs, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)
    final_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    final_output = sigmoid(final_layer_input)

    # Calculate error
    error = outputs - final_output
    final_output_delta = error * sigmoid_derivative(final_output)

    # Backward propagation
    hidden_layer_error = final_output_delta.dot(weights_hidden_output.T)
    hidden_layer_delta = hidden_layer_error * sigmoid_derivative(hidden_layer_output)

    # Update weights and biases
    weights_hidden_output += hidden_layer_output.T.dot(final_output_delta) * learning_rate
    bias_output += np.sum(final_output_delta, axis=0) * learning_rate
    weights_input_hidden += inputs.T.dot(hidden_layer_delta) * learning_rate
    bias_hidden += np.sum(hidden_layer_delta, axis=0) * learning_rate

    # Optionally print the error every 1000 epochs for monitoring
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Error: {np.mean(np.abs(error))}")

# Test the trained network
print("Final outputs after training:")
print(final_output)