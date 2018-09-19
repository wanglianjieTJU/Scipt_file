import os
rootdir = 'H:\database\mot//Academic vision//motData//xmlR'
i=1872096
dirlist = os.listdir(rootdir)
for n in range(0,len(dirlist)) :
    path = os.path.join(rootdir,dirlist[n])
    list = os.listdir(path)
    for item in list:
        n=n+1
        f=open(path+'//'+item)
        # lines=len(f.readlines())
        # a=a+lines
        # print a
        # print n
        line = f.readline()
        while line:
            ax = line.split(',')
            #print ax
            if int(ax[0])==0:
              i=i-1
            print i
            line = f.readline()
        f.close()