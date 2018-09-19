import os

traintxt=set(open('G://trainori.txt','r').readlines())
altxt=set(open('G://totalal.txt').readlines())
lines=traintxt-altxt
traintxt_w=open('G://train.txt','w')
for line in lines:
    traintxt_w.write(line[:11]+'\n')
traintxt_w.close()


