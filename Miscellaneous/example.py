import numpy as np

# Use sigmoidal activation
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Creating loss function
def loss(predicted, actual):
    return np.mean((predicted - actual) ** 2)

# Define the neural network architecture
input_size = 2
hidden_size = 3
output_size = 1

# Initialize the weights and biases with smaller random values
W1 = np.random.randn(input_size, hidden_size) * 0.01
b1 = np.random.randn(hidden_size) * 0.01
W2 = np.random.randn(hidden_size, output_size) * 0.01
b2 = np.random.randn(output_size) * 0.01

# Define the input for the AND gate
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Define the target output for the AND gate
target = np.array([[0], [0], [0], [1]])

# final_output
final_output=None

# Create some variables to track the best loss and the associated weights and biases
best_loss = float('inf')
best_W1 = None
best_b1 = None
best_W2 = None
best_b2 = None

# Define convergence threshold (5% error)
convergence_threshold = 0.05 * np.mean((target - np.mean(target)) ** 2)

iteration = 0
while iteration < 100:
    # Forward pass
    hidden_layer_output = np.dot(x, W1) + b1
    output = sigmoid(np.dot(hidden_layer_output, W2) + b2)

    # save final output
    final_output = output

    # Loss calculation
    current_loss = loss(output, target)

    if current_loss <= convergence_threshold:
        print('Converged at iteration:', iteration, 'with loss:', current_loss)
        break

    if current_loss < best_loss:
        print('New weights found, iteration:', iteration, 'loss:', current_loss)
        # Save current weights and biases as the best ones so far
        best_loss = current_loss
        best_W1 = W1.copy()
        best_b1 = b1.copy()
        best_W2 = W2.copy()
        best_b2 = b2.copy()

    # Update weights with smaller random values
    W1 += 0.01 * np.random.randn(input_size, hidden_size)
    b1 += 0.01 * np.random.randn(hidden_size)
    W2 += 0.01 * np.random.randn(hidden_size, output_size)
    b2 += 0.01 * np.random.randn(output_size)

    iteration += 1

print(final_output)