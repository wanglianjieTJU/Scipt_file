import os
import sys

def compare(file1,file2):
    f1=open(file1)
    f2=open(file2)
    lines1=f1.readlines()
    lines2=f2.readlines()
    print len(lines1)
    print len(lines2)
    output = sys.stdout
    outputfile = open('E:/more2.txt','w')
    sys.stdout = outputfile

    for line1 in lines1:

        if line1 not in lines2:
            line1 = line1.strip('\n')
            print line1
    outputfile.close()
    sys.stdout = output
def long_file(file):
    f=open(file)
    lines=f.readlines()
    print(len(lines))
def remove(file):
    f=open(file)
    lines=f.readlines()
    for line in lines:
        line = line.strip('\n')
        path="E:/train_P/"+line+'.jpg'

        print os.path.exists(path)
        os.remove(path)
        print path

if __name__ == '__main__':
    compare('E:/train2.txt','E:/train1.txt')
    long_file('E:/more2.txt')
    remove('E:/more2.txt')