# Sigmlidal activatino function
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Example usage
x = np.array([0.5, -1.0, 2.0])
output = sigmoid(x)
print(output)