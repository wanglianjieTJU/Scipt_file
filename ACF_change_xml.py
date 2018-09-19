import os

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys

file_srx = open(r"E:/train.txt")
line = file_srx.readline()
while line:
    f = line[:-1]
    tree = ET.parse(f)
    root = tree.getroot()
    print ("*" * 10)
    filename = root.find('filename').text
    filename = filename[:-4]
    print (filename)
    # file_object = open(filename + ".txt", 'w')
    file_object_log_car = open('F:/dateset/change_xml/car/train\\' + filename +'.txt', 'w')
    flag = False

    ########################################
    for size in root.findall('size'):
        width = size.find('width').text
        height = size.find('height').text
        #print (width, height)
    ########################################
    file_object_log_car.write("% bbGt version=3"+'\n')
    for object in root.findall('object'):

        name = object.find('category').text
        if name == 'ignored':
            bndbox = object.find('bndbox')
            xmin = bndbox.find('xmin').text
            ymin = bndbox.find('ymin').text
            xmax = bndbox.find('xmax').text
            ymax = bndbox.find('ymax').text
#            file_object_log_car.write(str(name) + " ")
#            file_object_log_car.write(str(xmin) + " ")
#            file_object_log_car.write(str(ymin) + " ")
#            file_object_log_car.write(str(xmax) + " ")
#            file_object_log_car.write(str(ymax) + " ")
#            file_object_log_car.write("\n")
        else:
            types = object.find('type').text
            occluded = object.find('occluded').text
            if occluded == 'no-occ':
                occluded = '0'
            elif occluded == 'partial-occ':
                occluded = '1'
            else:
                occluded = '2'
            truncated = object.find('truncated').text
            if truncated == 'truncated_0%':
                truncated = '0'
            elif truncated == 'truncated_1%~50%':
                truncated = '1'
            else:
                truncated = '2'

            bndbox = object.find('bndbox')
            xmin = bndbox.find('xmin').text
            ymin = bndbox.find('ymin').text
            xmax = bndbox.find('xmax').text
            ymax = bndbox.find('ymax').text
            #print (xmin, ymin, xmax, ymax)
            if types =='car'and occluded !=str(2) and truncated != str(2):
                file_object_log_car.write(str(types) + " ")
                file_object_log_car.write(str(xmin) + " ")
                file_object_log_car.write(str(ymin) + " ")
                file_object_log_car.write(str(xmax) + " ")
                file_object_log_car.write(str(ymax) +" 0 0 0 0 0 0 0")
                file_object_log_car.write("\n")
                flag=True




    # file_object.close( )
    file_object_log_car.close()
    if flag == False:
        os.remove('F:/dateset/change_xml/car/train\\'+filename + '.txt')
        # os.remove(filename + ".jpg")
        #os.remove(filename + ".log")
    if flag==True:
        flag=False
    line = file_srx.readline()
