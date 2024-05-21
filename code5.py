# this is more complex then previous one. It is variation of the previous code.
# I use a loop to get the weights, inputs and biases then feed into the neurons.
inputs = [1, 2, 3, 2.5]
weights = [
    [0.2, 0.8, -0.5, 1],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
]
biases = [2, 3, 0.5]

# Output of the current layer
layer_outputs = []


# For each neuron
for neuron_weights, neuron_bias in zip(weights, biases):
    # Zeroed output of the given neuron
    neuron_output = 0

    # For each input and weight to the neuron
    for n_input, weight in zip(inputs, neuron_weights):
        # Multiply this input by the associated weight
        # and add to the neuron's output variable

        neuron_output += n_input * weight

    # Add bias
    neuron_output += neuron_bias

    # Put the neuron's result into the layer's output list
    layer_outputs.append(neuron_output)

#print(layer_outputs)
w_out=[0.2, 0.8, -0.5]
biase_out=0.5
final_output=(layer_outputs[0]*w_out[0]+layer_outputs[1]*w_out[1]+layer_outputs[2]*w_out[2])+biase_out
print(final_output)