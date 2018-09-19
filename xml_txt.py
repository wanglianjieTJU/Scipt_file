import os

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys

file_srx = open(r"E:\test.txt")
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
    file_object_log = open(r'E:\Val_X\\' + filename + ".txt", 'w')
    flag = True

    ########################################
    for size in root.findall('size'):
        width = size.find('width').text
        height = size.find('height').text
        print (width, height)
    ########################################

    for object in root.findall('object'):

        name = object.find('category').text
        if name == 'ignored':
            bndbox = object.find('bndbox')
            xmin = bndbox.find('xmin').text
            ymin = bndbox.find('ymin').text
            xmax = bndbox.find('xmax').text
            ymax = bndbox.find('ymax').text
            file_object_log.write(str(name) + " ")
            file_object_log.write(str(xmin) + " ")
            file_object_log.write(str(ymin) + " ")
            file_object_log.write(str(xmax) + " ")
            file_object_log.write(str(ymax) + " ")
            file_object_log.write("\n")
            
            print ('write,w,,w,w,w,')
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
            else:
                truncated = '1'

            bndbox = object.find('bndbox')
            xmin = bndbox.find('xmin').text
            ymin = bndbox.find('ymin').text
            xmax = bndbox.find('xmax').text
            ymax = bndbox.find('ymax').text
            print (xmin, ymin, xmax, ymax)
            file_object_log.write(str(name) + " ")
            file_object_log.write(str(types) + " ")
            file_object_log.write(str(occluded) + " ")
            file_object_log.write(str(truncated) + " ")
            file_object_log.write(str(xmin) + " ")
            file_object_log.write(str(ymin) + " ")
            file_object_log.write(str(xmax) + " ")
            file_object_log.write(str(ymax) + " ")
            file_object_log.write("\n")

        if name == ("bicycle" or "motorbike"):
            # file_object.write("Cyclist" + " 0 0 0 " + xmin + ".00 " + ymin + ".00 " + xmax + ".00 " + ymax + ".00 " + "0 0 0 0 0 0 0" + "\n")
            file_object_log.write(str(float(int(xmax) - int(xmin)) * 1920.0 / float(width)) + " " + str(
                float(int(ymax) - int(ymin)) * 1080.0 / float(height)) + "\n")
            flag = True
            print ('write,w,,w,w,w,')
        if name == ("car"):
            # file_object.write("Car" + " 0 0 0 " + xmin + ".00 " + ymin + ".00 " + xmax + ".00 " + ymax + ".00 " + "0 0 0 0 0 0 0" + "\n")
            file_object_log.write(str(float(int(xmax) - int(xmin)) * 1920.0 / float(width)) + " " + str(
                float(int(ymax) - int(ymin)) * 1080.0 / float(height)) + "\n")
            flag = True
        if name == ("person"):
            # file_object.write("Pedestrian" + " 0 0 0 " + xmin + ".00 " + ymin + ".00 " + xmax + ".00 " + ymax + ".00 " + "0 0 0 0 0 0 0" + "\n")
            file_object_log.write(str(float(int(xmax) - int(xmin)) * 1920.0 / float(width)) + " " + str(
                float(int(ymax) - int(ymin)) * 1080.0 / float(height)) + "\n")
            flag = True
    # file_object.close( )
    file_object_log.close()
    if flag == False:
        # os.remove(filename + ".txt")
        # os.remove(filename + ".jpg")
        os.remove(filename + ".log")
    line = file_srx.readline()
