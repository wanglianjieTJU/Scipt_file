from PIL import Image
import numpy as np
#import Image

im = np.array(Image.open('G://vot2016\gymnastics4//00000151.png'))
n = 0
m = 0
[rows, cols] = im.shape
#n = np.zeros(8)
#m = np.zeros(8)
for i in range(rows):
    for j in range(cols):
        if (im[i, j] == 255):
            n = n + 1
        if(im[i,j] == 0):
            m = m +1
print(n)
print(m)