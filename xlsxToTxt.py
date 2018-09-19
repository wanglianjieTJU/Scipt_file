import numpy as np
import xlrd
data =  xlrd.open_workbook('G://unclaimed.xlsx')
sh = data.sheet_by_name("Sheet1")
print sh.nrows
print sh.ncols
n = 0
i = 0
file = open("G://unclaimed.txt", "w")
for n in range(1, sh.nrows):
    #for i in range(1, sh.ncols):
        text = sh.row_values(n)
        file.write(str(text[0]) + ' ' + str(text[1])+ ' ' +str(text[2])+ ' ' + str(text[3])+ ' ' + str(text[4])+  ' ' +str(text[5])+  ' ' +str(text[6])+ ' ' + str(text[7])+ ' ' + str(text[8]))
        file.write('\n')
print('over')