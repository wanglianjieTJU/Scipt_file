import numpy as np
import os
from PIL import Image
pathImg=r'G://davis//train_images'
pathgt=r'G://davis//train_labels'
files=os.listdir(pathgt)
for i,file in enumerate (files):
    gt = np.asarray(Image.open(pathgt + '\\' + file))
    imagename = os.path.splitext(file)[0] + ".jpg"
    img = np.asarray(Image.open(pathImg + '\\' + imagename))
    a=gt.shape[0]*gt.shape[1]
    b=img.shape[0]*img.shape[1]
    print(a,b)
    if a!=b:
        os.remove(pathgt + '\\' + file)
        imagename = os.path.splitext(file)[0] + ".jpg"
        os.remove(pathImg + '\\' + imagename)
        print('%s is removed ...' % file)
print('jieshu')