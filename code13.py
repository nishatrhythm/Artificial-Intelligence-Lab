# The Rectified Linear Unit (ReLU) activation function
import numpy as np

def relu(x):
    return np.maximum(0, x)

# Example usage
x = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])
output = relu(x)
print(output)