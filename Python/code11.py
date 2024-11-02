import numpy as np

input_neurons = 4
hidden1_neurons = 3
hidden2_neurons = 3
output_neurons = 1


weights_input_hidden1 = np.random.rand(input_neurons, hidden1_neurons)
biases_hidden1 = np.random.rand(hidden1_neurons)

weights_hidden1_hidden2 = np.random.rand(hidden1_neurons, hidden2_neurons)
biases_hidden2 = np.random.rand(hidden2_neurons)

weights_hidden2_output = np.random.rand(hidden2_neurons, output_neurons)
bias_output = np.random.rand(output_neurons)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

input_data = np.random.rand(10, input_neurons)

hidden1_output = np.dot(input_data, weights_input_hidden1) + biases_hidden1
hidden1_activation = sigmoid(hidden1_output)

hidden2_output = np.dot(hidden1_activation, weights_hidden1_hidden2) + biases_hidden2
hidden2_activation = sigmoid(hidden2_output)

output_layer_output = np.dot(hidden2_activation, weights_hidden2_output) + bias_output
output = sigmoid(output_layer_output)

print(output)