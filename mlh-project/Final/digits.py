import numpy as np
import pickle

with open('f_weights.txt', 'rb') as fp:
	weights = pickle.load(fp)

with open('f_biases.txt', 'rb') as fp:
	biases = pickle.load(fp)



def sigmoid(x):
	return 1.0/(1.0+np.exp(-x))

def feedforward(a):
	for b, w in zip(biases, weights):
		a = sigmoid(np.dot(w, a)+b)
	return a

