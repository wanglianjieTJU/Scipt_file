import os
rootdir = 'I://Test'
dirlist = os.listdir(rootdir)
#i=1
for n in range(0,len(dirlist)) :
    path = os.path.join(rootdir,dirlist[n])
    i=1
    if os.path.isdir(path) :
        filelist = os.listdir(path)
        for item in filelist:
            if item.endswith('.jpg') :
                src = os.path.join(os.path.abspath(path), item)
                dst = os.path.join(os.path.abspath(path),  str(i).zfill(7)+'.jpg')
                os.rename(src, dst)
                print 'converting %s to %s ...' % (src, dst)
                i = i + 1
print("jieshu")