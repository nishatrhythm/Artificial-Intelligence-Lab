import random

# Initial inputs, weights, and bias
inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0

# Calculate output with initial weights and bias
output = (inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + inputs[3] * weights[3] + bias)
print("Output with initial weights and bias:", output)

# Adjust weights and bias randomly
for i in range(len(weights)):
    weights[i] += random.uniform(-0.5, 0.5)
bias += random.uniform(-0.5, 0.5)

# Calculate output with adjusted weights and bias
output = (inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + inputs[3] * weights[3] + bias)
print("Output with adjusted weights and bias:", output)