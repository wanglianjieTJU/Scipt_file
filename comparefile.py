import os
import sys
import time
def compare(file1,file2):
    f1=open(file1)
    f2=open(file2)
    lines1=f1.readlines()
    lines2=f2.readlines()
    output = sys.stdout
    outputfile = open('E:/more1.txt','w')
    sys.stdout = outputfile

    for line1 in lines1:

        if line1 not in lines2:
            print line1
    outputfile.close()
    sys.stdout = output
if __name__ == '__main__':
    time_start = time.time()
    compare('E:/1.txt','E:/2.txt')
    time_end = time.time()
    a=time_end-time_start
    print('time cost', time_end - time_start,'s')
    outputfile = open('E:/more1.txt','a')
    outputfile.write(str(a)+'s'+'\n')