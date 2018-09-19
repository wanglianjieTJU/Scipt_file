# -*- coding: utf-8 -*-
"""
Created on Thu Feb 01 12:22:11 2018

@author: dell
"""

from xml.etree.ElementTree import ElementTree,Element
import os
import xml.etree.ElementTree as ET
path=r'F:\dateset\object detection\Academic version\newmydateset\1234'
count = 0
countcar = 0
cout_ign=0
countmotor=0
count_ped=0
count_tri=0
countpeople=0
count_vlt=0
countvan=0
counttruck=0
countothers=0
countbus=0
countbic=0
sum=0
files=os.listdir(path)
for file in files:
    aim_file=path+'\\'+file
    tree = ET.parse(aim_file)
    root = tree.getroot()
    for child in root.iter('object'):
        count=count+1
    for object in root.findall('object'):
            name = object.find('category').text
            
            if name =='ignored':
                cout_ign=cout_ign+1
                pass
            else :
                type=object.find('type').text
                if type == 'car':
                
                   countcar= countcar+1
                if type == 'motor':
                    countmotor= countmotor+1
                if type =='tricycle':
                    count_tri=count_tri+1
                if type =='Pedestrain':
                    count_ped=count_ped+1
                if type=='people':
                    countpeople=countpeople+1
                if type=='van-like-tricycle':
                    count_vlt=count_vlt+1
                if type=='Van':
                    countvan=countvan+1
                if type=='Truck':
                    counttruck=counttruck+1
                if type=='Others':
                    countothers=countothers+1
                if type=='Bus':
                    countbus=countbus+1
                if type=='bicycle':
                    countbic=countbic+1
#sum=cout_ign+countcar+count_tri+count_ped+countmotor+count_vlt+countpeople+countvan+counttruck+countbus+countbic+countothers
print '共计 ：' + str(count) + ' 个目标'
print '共计 ：' + str(cout_ign) + '个忽略区域'
print '共计 ：' + str(countcar) + '辆车'
print '共计 ：' + str(count_tri) + '辆三轮车'
print '共计 ：' + str(count_ped) + '个行人'
print '共计 ：' + str(countmotor) + '辆摩托车'
print '共计 ：' + str(count_vlt) + '辆带棚摩托车'
print '共计 ：' + str(countpeople) + '个人'
print '共计 ：' + str(countvan) + '辆面包车'
print '共计 ：' + str(counttruck) + '辆卡车'
print '共计 ：' + str(countbus) + '辆公共汽车'
print '共计 ：' + str(countbic) + '辆自行车'
print '共计 ：' + str(countothers) + '其他'
#print '共计 ：' + str(sum)