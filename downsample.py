import os
pathImg='F://test//'
dirlist = os.listdir(pathImg)
for i in range(0,len(dirlist)) :
    path = os.path.join(pathImg,dirlist[i])
    if os.path.isdir(path) :
        print'The ongoing sequence is ',dirlist[i]
        filelist = os.listdir(path)
        for item in filelist:
            if item.endswith('.png') :
                if int(item[:7])%2 == 0:
                        os.remove(pathImg + '\\' + dirlist[i]+'\\'+item)
                        print('%s is removed ...' % item)
print('jieshu')

