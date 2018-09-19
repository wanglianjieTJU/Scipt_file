import random
# fp=open('F://train.txt','r')
# for idx,line in enumerate(fp):
#     if idx%2==0:
#         fq = open('F://b.txt','a')
#         fq.write(line)
# fp.close()
# fq.close()

def ReadFileDatas():
    FileNamelist = []
    file = open('F://train.txt', 'r+')
    for line in file:
        line = line.strip('\n')
        FileNamelist.append(line)
    print('len ( FileNamelist ) = ', len(FileNamelist))
    file.close()
    return FileNamelist


def WriteDatasToFile(listInfo):
    file_handle = open('F://b.txt', mode='a')
    for idx in range(len(listInfo)):
        str = listInfo[idx]
        ndex = str.rfind('_')
        # print('ndex = ',ndex)
        #str_houZhui = str[(ndex + 1):]
        # print('str_houZhui = ',str_houZhui)
        str_Result = str + '\n'
        print(str_Result)
        file_handle.write(str_Result)
    file_handle.close()


if __name__ == "__main__":
    listFileInfo = ReadFileDatas()
    random.shuffle(listFileInfo)
    WriteDatasToFile(listFileInfo)
