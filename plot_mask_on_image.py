import cv2
import numpy as np
from PIL import Image
import numpy as np
def get_blue(img):
    b = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
    b[:,:] = img[:,:,0]
    return b[:,:]
def get_green(img):
    g = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
    g[:,:] = img[:,:,1]
    return g[:,:]
def get_red(img):
    r = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
    r[:,:] = img[:,:,2]
    return r[:,:]
mask = np.array(Image.open('G://davis//DAVIS-data//DAVIS//Annotations//480p//bear//00000001.png'))
mask =np.where(mask>0,255,50)
img = np.array(Image.open('G://davis//DAVIS-data//DAVIS//JPEGImages//480p//bear//00000001.jpg'))
#b, g, r = cv2.split(img)
b = get_blue(img)
g = get_green(img)
r = get_red(img)
b =np.multiply(b,mask)
g= np.multiply(g,mask)
r= np.multiply(r,mask)
#cv2.imshow("Blue 1", b)
#cv2.imshow("Green 1", g)
#cv2.imshow("Red 1", r)
merged = cv2.merge([b,g,r])
mergedByNp = np.dstack([b,g,r])
cv2.imshow("zuhe 1", merged)
cv2.imshow("zuhe 2", mergedByNp)
cv2.waitKey (0)
cv2.destroyAllWindows()
