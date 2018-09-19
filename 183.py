import numpy as np
import os
from PIL import Image
pathgt = 'D:\liuweidownload//2017coco\stuff_annotations_trainval2017//annotations\stuff_train2017_pixelmaps\stuff_train2017_pixelmaps'
dirlist = os.listdir(pathgt)
for item in dirlist:
    if item.endswith('.png'):
        gt = Image.open(pathgt + '//' + item)
        gt = np.asarray(gt)
        a = gt.size
        m = gt == 183
        n = gt[m]
        n = n.size
        if n != 0:
            print(item)
print('over')