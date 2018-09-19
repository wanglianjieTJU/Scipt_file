# import numpy as np
# import os
# from PIL import Image
# pathgt=r'G://davis//test_label'
# pathImg=r'G://davis//test_img'
# files=os.listdir(pathgt)
# for i,file in enumerate (files):
#     gt = np.asarray(Image.open(pathgt + '\\' + file))
#     a=gt.size
#     m= gt ==255
#     n=gt[m]
#     n=n.size
#     print(i,n)
#     if n==0:
#         os.remove(pathgt + '\\' + file)
#         imagename = os.path.splitext(file)[0] + ".jpg"
#         os.remove(pathImg + '\\' + imagename)
#         print('%s is removed ...' % file)
# print('jieshu')
import numpy as np
import os
from PIL import Image
pathgt = 'G://davis//DAVIS-data//DAVIS//Annotations//480p'
pathImg='G://davis//DAVIS-data//DAVIS//JPEGImages//480p'
dirlist = os.listdir(pathgt)
for i in range(0,len(dirlist)) :
    path = os.path.join(pathgt,dirlist[i])
    if os.path.isdir(path) :
        print'The ongoing sequence is ',dirlist[i]
        filelist = os.listdir(path)
        for item in filelist:
            if item.endswith('.png') :
                gt=Image.open(path+'//'+item)
                gt=np.asarray(gt)
                a=gt.size
                m= gt ==255
                n=gt[m]
                n=n.size
                if n==0:
                        os.remove(pathgt + '\\' + dirlist[i]+'\\'+item)
                        imagename = os.path.splitext(item)[0] + ".jpg"
                        os.remove(pathImg + '\\' + dirlist[i]+'\\'+imagename)
                        print('%s is removed ...' % item)
print('jieshu')

