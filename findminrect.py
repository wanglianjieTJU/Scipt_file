import numpy as np
import os
from PIL import Image
rootdir = 'G://davis//DAVIS-data//DAVIS//Annotations//480p'
dirlist = os.listdir(rootdir)
for n in range(0,len(dirlist)) :
    path = os.path.join(rootdir,dirlist[n])
    if os.path.isdir(path) :
        gt_write = open(r'G://davis//DAVIS-data//DAVIS//Annotations//davisgt480p//' + dirlist[n] + '.txt', 'w')
        print'The ongoing sequence is ',dirlist[n]
        filelist = os.listdir(path)
        for item in filelist:
            if item.endswith('.png') :
                gt=Image.open(path+'//'+item)
                gt=np.asarray(gt)
                rows=gt.shape[0]
                cols=gt.shape[1]
                a=[]
                b=[]
                for i in range(0,rows):
                    for j in range(0,cols):
                       if (gt[i][j] == 255):
                        a.append(i)
                        b.append(j)
                maxi=np.max(a)
                mini=np.min(a)
                maxj=np.max(b)
                minj=np.min(b)
                w=maxj-minj
                h=maxi-mini
                print(item,'writing',minj,mini,w,h)
                gt_write.writelines(str(minj) + ",")
                gt_write.writelines(str(mini) + ",")
                gt_write.writelines(str(w) + ",")
                gt_write.writelines(str(h) + '\n')
        gt_write.close()
print('end')