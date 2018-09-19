import os
import shutil
acadir = 'F://2222'
HDdir = 'F://1111'
savedir ='F://3333'
dirlist = os.listdir(acadir)
for n in range(0,len(dirlist)) :
    startnumber=dirlist[0]
    startnumber=int(startnumber[12:16])
    path = os.path.join(acadir,dirlist[n])
    scrpath =os.path.join(HDdir,dirlist[n])
    savepath = os.makedirs(savedir +'//' + dirlist[n])
    savepath = os.path.join(savedir,dirlist[n])
    if os.path.isdir(path) :
        filelist = os.listdir(path)
        copynumber =len(filelist)
        endnumber =copynumber*2+startnumber
        totalfiles =os.listdir(scrpath)
        for item in totalfiles:
            if int(item[:4])>=startnumber and int(item[:4])<=endnumber:
                src = os.path.join(os.path.abspath(scrpath), item)
                dst = os.path.join(os.path.abspath(savepath))
                shutil.copy(src, dst)
                print 'copyfile %s to %s ...' % (src, dst)
print('jieshu')