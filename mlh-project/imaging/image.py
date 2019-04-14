import numpy as np
from PIL import Image
import pickle


img = Image.open('sample2.png').convert('L')

#print np.array(img)
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
		a.append([np.abs(214-value)])

with open("array.txt", "wb") as fp:
	pickle.dump(a, fp)


