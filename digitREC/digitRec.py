import numpy as np
from PIL import Image
import pickle

img_original = Image.open('digit.png')
img = img_original.resize((28, 28)).convert('L')

img_arr = np.array(img)

#print img_arr.flatten()

WIDTH, HEIGHT = img.size

data = list(img.getdata()) # convert image data to a list of integers
# convert that to 2D list (list of lists of integers)
data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]

# At this point the image's pixels are all in memory and can be accessed
# individually using data[row][col].

# For example:
a = []
for row in data:
	for value in row:
		a.append([np.abs(214-value)/214])

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


print(np.argmax(feedforward(a)))
