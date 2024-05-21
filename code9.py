# inputs-batch with weights and then transpose them to calculate dot product.
import numpy as np


inputs = np.array([[1.0, 2.0, 3.0, 2.5],
                   [2.0, 4.0, 1.5, 2.0],
                   [0.5, 1.5, 2.0, 3.5],
                   [0.5, 1.5, 2.0, 3.5],
                   [0.5, 1.5, 2.0, 3.5]])

weights = np.array([[0.2, 0.8, -0.5, 1.0],
                    [0.5, -0.9, 0.3, -0.7],
                    [-0.1, 0.6, -0.3, 0.9]])

biases = np.array([2.0, 1.0, -0.5])

outputs = np.dot(inputs, weights.T)+biases
print(outputs)