import shutil
srcdir='G://vot//imgcrop2//'
f = open('G://vot//test3//test.txt')
for line in open('G://vot//test3//test.txt'):
    line = f.readline()
    imagename = line[0:8]  +".jpg"
    src = srcdir+imagename
    print(src)
    dst = 'G://vot//test3//image'
    shutil.copy(src, dst)
    print 'copyfile %s to %s ...' % (src, dst)
    #print(imagename)