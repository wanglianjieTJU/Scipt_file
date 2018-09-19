
"""
Created on  2018

@author: hp
"""
from PIL import Image
from PIL import ImageChops
import os
import shutil

MIRROR_FLAGE = True
TRANSPOSE_FLAGE = True
OFFSET_FlAGE = True
# work_path='image_conver'
# work_dir_name='Train'
# work_dir_label_name='Train_Truth'
# convert_image_dir_name='convert_image'
# cwd=os.getcwd()
# work_dir_path=cwd+os.sep+work_path+os.sep+work_dir_name
# convert_image_dir_path=cwd+os.sep+work_path+os.sep+convert_image_dir_name#

# image_number=0
# if os.path.exists(convert_image_dir_path):
#     shutil.rmtree(convert_image_dir_path)
# os.mkdir(convert_image_dir_path)


# image_file_name=os.listdir(work_dir_path)
# image_file_name_path=[]
# for x in image_file_name:
#     image_file_name_path.append(work_dir_path+os.sep+x)



pathImg=r'G://votimg'
files=os.listdir(pathImg)
for file in files:
    flag = os.path.splitext(file)[0]
    imagename =os.path.splitext(file)[0] + ".jpg"
    #print(imagename)
    img= Image.open(pathImg+'\\'+ imagename)
    #print(image)
    if MIRROR_FLAGE:
        img_mirror = img.transpose(Image.FLIP_LEFT_RIGHT)
        img_mirror.save(flag + "1.jpg")
    if TRANSPOSE_FLAGE:
        img_rotate_3 = img.rotate(3)
        img_rotate_3.save(flag + "2.jpg")

    if OFFSET_FlAGE:
        img_offset = ImageChops.offset(img, xoffset=1, yoffset=1)
        img_rotate_3.save(flag + "3.jpg")