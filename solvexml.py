# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 21:38:27 2018

@author: dell
"""

from xml.etree.ElementTree import ElementTree,Element
import os
import xml.etree.ElementTree as ET
path=r'F:\xml'
files=os.listdir(path)
for file in files:
    aim_file=path+'\\'+file
    tree = ET.parse(aim_file)
    root = tree.getroot()
    for child in root:
       #print(child.tag, child.attrib)
        for rank in root.iter(tag='box'):
            print rank.attrib['xtl']
           # print rank.tag,

          # '['ytr']'

    #     new_elem=(int(elem.text)*2)
    #     rank.text = str(new_elem)
    # for rank in root.iter('yt1'):
    #     new_elem=(int(elem.text)*2)
    #     rank.text = str(new_elem)
    # for elem in root.iter('xbr'):
    #     new_elem=(int(elem.text)*2)
    #     elem.text = str(new_elem)
    # for elem in root.iter('ybr'):
    #     new_elem=(int(elem.text)*2)
    #     elem.text = str(new_elem)
    # for elem in root.iter('xmax'):
    #     new_elem=(int(elem.text)/2+int(elem.text)%2)
    #     elem.text = str(new_elem)
    # for elem in root.iter('ymax'):
    #     new_elem=(int(elem.text)/2+int(elem.text)%2)
    #     elem.text = str(new_elem)
    tree.write(aim_file)