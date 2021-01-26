import numpy as np

X = np.array([[0,0], [0,1], [1,1], [1,0]])
y = np.array([[0,0], [1,0], [0,1], [1,1]])

#Sigmoid Function
def sigmoid (x):
    return 1/(1 + np.exp(-x))

#Derivative of Sigmoid Function
def derivatives_sigmoid(x):
    return x * (1 - x)

epoch=50000
lr=0.5
inputlayer_neurons = X.shape[1] 
hiddenlayer_neurons = 3
output_neurons = y.shape[1]

wh=np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
wout=np.random.uniform(size=(hiddenlayer_neurons,output_neurons))

 
for i in range(epoch):
    #Forward Propogation
    hidden_layer_input = np.dot(X,wh)
    hiddenlayer_activations = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hiddenlayer_activations,wout)
    output = sigmoid(output_layer_input)


#Backpropagation
    E = y-output
    slope_output_layer = derivatives_sigmoid(output)
    slope_hidden_layer = derivatives_sigmoid(hiddenlayer_activations)
    d_output = E * slope_output_layer
    Error_at_hidden_layer = d_output.dot(wout.T)
    d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer
    wout += hiddenlayer_activations.T.dot(d_output) *lr
    wh += X.T.dot(d_hiddenlayer) *lr

print("Output of Neural Network after given epoch:\n", output)

