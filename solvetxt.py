import os
from PIL import Image
inputDir = "I://Test//oldtxt"
outputDir ='I://Test//newtxt'
newphotopath = 'I:\Test\New'
oldphotopath ='I:\Test\Old'
dirlist = os.listdir(inputDir)
for file in dirlist:
    print file[:18]
    newimage = Image.open(newphotopath+'//'+file[:18]+'//'+'img0000001.jpg')
    oldimage = Image.open(oldphotopath+'//'+file[:18]+'//'+'0000001.jpg')
    multiple =int(newimage.size[0])/int(oldimage.size[0])
    print ('multiple is %s' %multiple)
    inputStream = open(inputDir + '//' + file , 'r+')
    outputStream = open(outputDir + '//' + file , 'w+')
    for strings in inputStream.readlines():
        ax = strings.split(',')
        ax[4]=int(ax[4])*multiple
        ax[5]=int(ax[5])*multiple
        outputStream.write(ax[0]+',')
        outputStream.write(ax[1] + ',')
        outputStream.write(ax[2] + ',')
        outputStream.write(ax[3] + ',')
        outputStream.write(str(ax[4]) + ',')
        outputStream.write(str(ax[5]) + ',')
        outputStream.write(ax[6] + ',')
        outputStream.write(ax[7])
    inputStream.close()
    outputStream.close()
    print inputStream
    print(' is over')
print 'over'
