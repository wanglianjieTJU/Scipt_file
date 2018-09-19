import cv2
import numpy as np
import os
pathgt=r'G:\label'
pathImg=r'G:\image'
files=os.listdir(pathgt)
for file in files:
    gt = cv2.imread(pathgt+'\\'+file)
    img_h, img_w, _ = gt.shape
    imagename =os.path.splitext(file)[0] + ".jpg"
    print(imagename)
    image = cv2.imread(pathImg+'\\'+ imagename)
    print(image)
    #cv2.imshow('a',image)
    #cv2.waitKey(0)
    gtgray = cv2.cvtColor(gt, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('a',gtgray)
#cv2.waitKey(0)
    ret, thresh = cv2.threshold(gtgray, 127, 255, cv2.THRESH_BINARY)
    #cv2.imshow('b',thresh)
#cv2.waitKey(0)
    gt, cnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# import pdb
# pdb.set_trace()
#_a, cnts, _b = x
    c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

# compute the rotated bounding box of the largest contour
    rect = cv2.minAreaRect(c)
# rect = cv2.minAreaRect(cnts[1])
    box = np.int0(cv2.boxPoints(rect))

# draw a bounding box arounded the detected barcode and display the image
    cv2.drawContours(gt, [box], -1, (0, 255, 0), 3)
    #cv2.imshow("Image", gt)
#cv2.imwrite("contoursImage2.jpg", image)
    #cv2.waitKey(0)

    Xs = [i[0] for i in box]
    Ys = [i[1] for i in box]
    x1 = min(Xs)
    x2 = max(Xs)
    y1 = min(Ys)
    y2 = max(Ys)
    hight = y2 - y1
    width = x2 - x1
    #cropgt = gt[y1-(hight/2):y1 + hight+(hight/2), x1-(width/2):x1 + width+(width/2)]
    #cropImg = image[y1-(hight/2):y1 + hight+(hight/2), x1-(width/2):x1 + width+(width/2)]
    if x1-width>0 and x1+width*2<=img_w and y1-hight>0 and y1+hight*2<=img_h:
        cropgt = gt[y1-hight:y1 + hight*2, x1-width:x1 + width*2]
        cropImg = image[y1-hight:y1 + hight*2, x1-width:x1 + width*2]
    else:
        min_x_val = max(0, x1-width)
        min_y_val = max(0, y1-hight)
        max_x_val = min(img_w, x1+width*2)
        max_y_val = min(img_h, y1+hight*2)
        cropgt = gt[min_y_val:max_y_val,min_x_val:max_x_val]
        cropImg = image[min_y_val:max_y_val,min_x_val:max_x_val]
# show image
#cv2.imshow("cropImg", cropImg)
    cv2.imwrite("G://label1"+ "//"+ file, cropgt)
    cv2.imwrite("G://image1"+ "//" + imagename, cropImg)
