import random

# Inputs
inputs = [1, 2, 3, 2.5]

# Randomly initialize weights and biases for the hidden layer
hidden_weights = [[random.uniform(-1, 1) for _ in range(4)] for _ in range(3)]
hidden_biases = [random.uniform(-1, 1) for _ in range(3)]

# Randomly initialize weights and bias for the output layer
output_weights = [random.uniform(-1, 1) for _ in range(3)]
output_bias = random.uniform(-1, 1)

# Calculate outputs for the hidden layer
hidden_outputs = [
    sum([inputs[i] * hidden_weights[j][i] for i in range(4)]) + hidden_biases[j]
    for j in range(3)
]

# Calculate output for the output layer
output = sum([hidden_outputs[j] * output_weights[j] for j in range(3)]) + output_bias

print("Output:", output)