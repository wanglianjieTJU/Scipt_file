# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 09:42:10 2018

@author: dell
"""

import os
import sys
import re
'''
    扫描文件夹dir中所有文件，返回文件的相对路径列表
'''
def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):         # 如果是文件则添加进 fileList
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):   # 如果是文件夹
            newDir = os.path.join(dir, s)
            GetFileList(newDir, fileList)
    return fileList
output = sys.stdout
outputfile = open('E:/train.txt', 'w')
sys.stdout = outputfile

list = GetFileList('F:/dateset/object detection/Academic version/newmydateset/train_X', []) # 获取所有myFolder文件夹下所有文件名称（包含拓展名）

# 输出所有文件夹中的路径（相对于当前运行的.py文件的相对路径）
for route in list:
    # route 为路径

    #num = re.sub('(.*)\\\\', "", route)
   #num1 = re.sub('(\.)(.*)', "", num)

    print(route)

# 关闭输出重定向
#print '---'
outputfile.close()
sys.stdout = output
