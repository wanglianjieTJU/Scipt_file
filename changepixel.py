from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.array(Image.open('G://00000004.png'))
print(img[1][1])
width = img.shape[0]
height = img.shape[1]
print(width)
print(height)
for i in range(0,width):
    for j in range(0,height):
        if( img[i][j] == 255):
            img[i][j] = 1
img=img.covert('L')
img.save("G://000000041.png")
