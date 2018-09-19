import numpy as np
import os
rootdir = 'F:/codedownload/vot2016/'
seqlist_path ='G:/vot.txt'
with open(seqlist_path,'r') as fp:
    seq_list = fp.read().splitlines()
for i,seq in enumerate(seq_list):
    gt_write = open(r'G:/vot-otbdouble/' + seq + ".txt", 'w')
    gt=np.loadtxt(rootdir + seq + '/groundtruth.txt',delimiter=',')
    rlen=gt.shape[0]
    print(rlen)
    if gt.shape[1]==8:
        for num in range(0,gt.shape[0]):
            # xmin = int(round(np.min(gt[num,[0,2,4,6]])))
            # ymin = int(round(np.min(gt[num,[1,3,5,7]])))
            # xmax = int(round(np.max(gt[num,[0,2,4,6]])))
            # ymax = int(round(np.max(gt[num,[1,3,5,7]])))
            xmin = np.min(gt[num,[0,2,4,6]])
            ymin = np.min(gt[num,[1,3,5,7]])
            xmax = np.max(gt[num,[0,2,4,6]])
            ymax = np.max(gt[num,[1,3,5,7]])
            w = xmax-xmin
            h = ymax-ymin
            w=('%.3f' %w)
            h=('%.3f' %h)
            print(w,h)
            gt_write.write(str(xmin) + ",")
            gt_write.write(str(ymin) + ",")
            gt_write.write(str(w) + ",")
            gt_write.write(str(h) + '\n')
print('jieshu')