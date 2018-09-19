import cv2
import os
rootdir = 'H://database//test//'
savepath= 'H://database//save'
i=-1
dirlist = os.listdir(rootdir)
for n in range(0, len(dirlist)):
    path = os.path.join(rootdir, dirlist[n])
    i = i+1
    save_path = os.makedirs(savepath + '//'+str(i).zfill(3))
    print save_path
    cap = cv2.VideoCapture(path)
    print cap.isOpened()
    frame_count = 1
    success = True
    while (success):
        success, frame = cap.read()
        #print 'Read a new frame: ', success
        params = []
        # params.append(cv.CV_IMWRITE_PXM_BINARY)
        params.append(1)
        cv2.imwrite(savepath + '//'+str(i).zfill(3)+'//' + str(frame_count).zfill(5)+'.jpg', frame)
        frame_count = frame_count + 1
        #print"success"

cap.release()