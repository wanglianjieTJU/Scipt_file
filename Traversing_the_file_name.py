# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 09:42:10 2018

@author: dell
"""

import os
def GetFileList(dir, fileList):
    for s in os.listdir(dir):
        a = s.split('.')
        b = a[0]
        fileList.append(b)
    return fileList
outputfile = open('E://googledownload//panoptic_annotations_trainval2017//annotations//panoptic_train2017//train.txt', 'w+')
list = GetFileList('E://googledownload//panoptic_annotations_trainval2017//annotations//panoptic_train2017//panoptic_train2017', [])
for route in list:
    outputfile.writelines(route[:]+'\n')
outputfile.close()
print("jieshu")