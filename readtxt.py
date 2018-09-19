# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 15:29:17 2018

@author: dell
"""

# coding: utf-8
import cv2
import os
inputDir = "H://datebase//sot//Academic vision//RELEASE//"
inputAnnDir = "H://datebase//sot//Academic vision//RELEASE//sot_ann_release//"
pickfile = "train//uav0000169_00000_s"
inputStream = open(inputAnnDir + pickfile + '.txt','r')
fileList = os.listdir(inputDir + pickfile)#遍历图片
for i in range(1,len(fileList)):
    img1 = cv2.imread(inputDir + pickfile + '//img' + str(i).zfill(7) + '.jpg')
    line = inputStream.readline()#一行一行的读
    line = line.strip('\n')
    ax = line.split(',')
    cv2.rectangle(img1, (int(ax[0]), int(ax[1])), (int(ax[0]) + int(ax[2]), int(ax[1]) + int(ax[3])), (0, 0, 255), 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img1, 'car', (int(ax[0]) - 1, int(ax[1]) - 5), font, 0.8, (0, 255, 255), 2)
    img = cv2.resize(img1, (722, 482), interpolation=cv2.INTER_AREA)
    cv2.imshow('a',img)
    cv2.waitKey(1)
    print i
inputStream.close()
cv2.destroyAllWindows()