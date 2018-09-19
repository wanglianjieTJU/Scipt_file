# -*- coding: utf-8 -*-
import cv2
inputDir = "H://1111//test"
pickfile = "uav0000006_06900_v"
f=open("H://1111//txt//uav0000006_06900_v.txt")
line = f.readline()
cur_indx = 1
pre_indx = 1
img1 = cv2.imread(inputDir + '//' + pickfile + '//' + "img0000001"+ '.jpg')
while line:
    ax = line.split(',')
    print ax
    ax[0] = str(int(ax[0]) + 1)
    pre_indx = cur_indx
    cur_indx = int(ax[0])
    if cur_indx != pre_indx:
        img = cv2.resize(img1, (1348,740), interpolation=cv2.INTER_AREA)
        cv2.imshow('a', img)
        cv2.waitKey(1)
        img1 = cv2.imread(inputDir + '//' + pickfile+ '//'+'img' + str(ax[0]).zfill(7) + '.jpg')
        print inputDir + '//' + pickfile+ '//' + str(ax[0]).zfill(7) + '.jpg'
    if int(ax[7])== 0:
        cv2.rectangle(img1, (int(ax[2]), int(ax[3])), (int(ax[2]) + int(ax[4]), int(ax[3]) + int(ax[5])), (0, 0, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img1, 'ignore', (int(ax[2]) - 1, int(ax[3]) - 5), font, 0.8, (0, 255, 255), 2)

    elif int(ax[7])== 1:
        cv2.rectangle(img1, (int(ax[2]), int(ax[3])), (int(ax[2]) + int(ax[4]), int(ax[3]) + int(ax[5])), (255,0,0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img1, 'pedestrian', (int(ax[2]) - 1, int(ax[3]) - 5), font, 0.8, (0, 255, 255), 2)
    elif int(ax[7])== 2:
        cv2.rectangle(img1, (int(ax[2]), int(ax[3])), (int(ax[2]) + int(ax[4]), int(ax[3]) + int(ax[5])), (255,0,255),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img1, 'people', (int(ax[2]) - 1, int(ax[3]) - 5), font, 0.8, (0, 255, 255), 2)
    elif int(ax[7]) == 3:
        cv2.rectangle(img1, (int(ax[2]), int(ax[3])), (int(ax[2]) + int(ax[4]), int(ax[3]) + int(ax[5])), (0,205,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img1, 'bicycle', (int(ax[2]) - 1, int(ax[3]) - 5), font, 0.8, (0, 255, 255), 2)
    elif int(ax[7]) == 4:
        cv2.rectangle(img1, (int(ax[2]), int(ax[3])), (int(ax[2]) + int(ax[4]), int(ax[3]) + int(ax[5])), (0,139,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img1, 'car', (int(ax[2]) - 1, int(ax[3]) - 5), font, 0.8, (0, 255, 255), 2)
       # print "print car"
    elif int(ax[7]) == 5:
        cv2.rectangle(img1, (int(ax[2]), int(ax[3])), (int(ax[2]) + int(ax[4]), int(ax[3]) + int(ax[5])), (0,255,255),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img1, 'van', (int(ax[2]) - 1, int(ax[3]) - 5), font, 0.8, (0, 255, 255), 2)
    elif int(ax[7]) == 6:
        cv2.rectangle(img1, (int(ax[2]), int(ax[3])), (int(ax[2]) + int(ax[4]), int(ax[3]) + int(ax[5])), (148,0,211),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img1, 'truck', (int(ax[2]) - 1, int(ax[3]) - 5), font, 0.8, (0, 255, 255), 2)
        #print "print turnk"
    elif int(ax[7]) == 7:
        cv2.rectangle(img1, (int(ax[2]), int(ax[3])), (int(ax[2]) + int(ax[4]), int(ax[3]) + int(ax[5])), (205,102,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img1, 'tricycle', (int(ax[2]) - 1, int(ax[3]) - 5), font, 0.8, (0, 255, 255), 2)
    elif int(ax[7]) == 8:
        cv2.rectangle(img1, (int(ax[2]), int(ax[3])), (int(ax[2]) + int(ax[4]), int(ax[3]) + int(ax[5])), (160,32,640),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img1, 'van-like-tricycle', (int(ax[2]) - 1, int(ax[3]) - 5), font, 0.8, (0, 255, 255), 2)
    elif int(ax[7]) == 9:
        cv2.rectangle(img1, (int(ax[2]), int(ax[3])), (int(ax[2]) + int(ax[4]), int(ax[3]) + int(ax[5])),(139,0,0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img1, 'bus', (int(ax[2]) - 1, int(ax[3]) - 5), font, 0.8, (0, 255, 255), 2)
    elif int(ax[7]) == 10:
        cv2.rectangle(img1, (int(ax[2]), int(ax[3])), (int(ax[2]) + int(ax[4]), int(ax[3]) + int(ax[5])),(255,255,0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img1, 'motor', (int(ax[2]) - 1, int(ax[3]) - 5), font, 0.8, (0, 255, 255), 2)
    elif int(ax[7]) == 11:
        cv2.rectangle(img1, (int(ax[2]), int(ax[3])), (int(ax[2]) + int(ax[4]), int(ax[3]) + int(ax[5])),(104,34,139), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img1, 'others', (int(ax[2]) - 1, int(ax[3]) - 5), font, 0.8, (0, 255, 255), 2)
    line = f.readline()
f.close()