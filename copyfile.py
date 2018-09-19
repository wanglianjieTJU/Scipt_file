import os
import shutil
rootdir = 'G://vot//votseg_dataset'
dirlist = os.listdir(rootdir)
for n in range(0,len(dirlist)) :
    path = os.path.join(rootdir,dirlist[n])
    if os.path.isdir(path) :
        filelist = os.listdir(path)
        for item in filelist:
            if item.endswith('.png') :
                src = os.path.join(os.path.abspath(path), item)
                dst = 'G://vot//votmask'
                shutil.copy(src, dst)
                print 'copyfile %s to %s ...' % (src, dst)
print('jieshu')