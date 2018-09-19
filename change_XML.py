# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 21:38:27 2018

@author: dell
"""

from xml.etree.ElementTree import ElementTree,Element
import os
import xml.etree.ElementTree as ET
path=r'H:/datebase/object detection/mydatasets/Val_X'
files=os.listdir(path)
for file in files:
    aim_file=path+'\\'+file
    tree = ET.parse(aim_file)
    root = tree.getroot()
    for child in root:
       print(child.tag, child.attrib)
    for rank in root.iter('width'):
        new_elem=(int(rank.text)/2+int(rank.text)%2)
        rank.text = str(new_elem)
    for rank in root.iter('height'):
        new_elem=(int(rank.text)/2+int(rank.text)%2)
        rank.text = str(new_elem)
    for elem in root.iter('xmin'):
        new_elem=(int(elem.text)/2+int(elem.text)%2)
        elem.text = str(new_elem)
    for elem in root.iter('ymin'):
        new_elem=(int(elem.text)/2+int(elem.text)%2)
        elem.text = str(new_elem)
    for elem in root.iter('xmax'):
        new_elem=(int(elem.text)/2+int(elem.text)%2)
        elem.text = str(new_elem)
    for elem in root.iter('ymax'):
        new_elem=(int(elem.text)/2+int(elem.text)%2)
        elem.text = str(new_elem)
    tree.write(aim_file)