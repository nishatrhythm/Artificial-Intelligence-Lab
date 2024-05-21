# For solving logic gates, the activation function that is commonly used is the step function or the binary step function. The step function is a threshold-based function that outputs 0 if the input is less than or equal to a certain threshold and outputs 1 if the input is greater than the threshold.

# we will use it to solve logic gates problems.
def step_function(x, threshold=0):
    if x <= threshold:
        return 0
    else:
        return 1

# Example usage
x = 0.5
output = step_function(x)
print(output)