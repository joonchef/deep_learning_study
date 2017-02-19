import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('sample.jpeg')

plt.imshow(img)
plt.show()
