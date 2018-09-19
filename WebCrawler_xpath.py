import requests
from lxml import etree
from requests.exceptions import RequestException
import multiprocessing
import time
import pandas as pd

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip',
'Connection':'close',
'Referer':'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;amp;wd=&amp;amp;eqid=c3435a7d00146bd600000003582bfd1f'
}

url='http://nj.jianjia.com/ershoufang/'
page=('pg')
for i in range(1,11):
    if i == 1:
        i=str(i)
        a=(url+page+i+'/')
        while 1:
            try:
                page = requests.get(url=a,headers=headers)
            except:
                print("Connection refused by the server..")
                print("Let me sleep for 5 seconds")
                print("ZZzzzz...")
                time.sleep(5)
                print("Was a nice sleep, now let me continue...")
                continue
        #r=requests.get(url=a,headers=headers)
                html=r.content
    else:
        i=str(i)
        a=(url+page+i+'/')
        while 1:
            try:
                page = requests.get(url=a,headers=headers)
            except:
                print("Connection refused by the server..")
                print("Let me sleep for 5 seconds")
                print("ZZzzzz...")
                time.sleep(5)
                print("Was a nice sleep, now let me continue...")
                continue
        #r=requests.get(url=a,headers=headers)
                html2=r.content
                html = html + html2
    time.sleep(0.5)
encoding = requests.get(url, headers=headers).encoding
lj = etree.HTML(html, parser=etree.HTMLParser(encoding=encoding))
price=lj.xpath('//div[@class="priceInfo"]')

tp=[]
for a in price:
    totalPrice=a.xpath('.//span/text()')[0]
    tp.append(totalPrice)
houseInfo=lj.xpath('//div[@class="houseInfo"]')

hi=[]
for b in houseInfo:
    house=b.xpath('.//text()')[0]+b.xpath('.//text()')[1]
    hi.append(house)
followInfo=lj.xpath('//div[@class="followInfo"]')

fi=[]
for c in followInfo:
    follow=c.xpath('./text()')[0]
    fi.append(follow)
house=pd.DataFrame({'totalprice':tp,'houseinfo':hi,'followinfo':fi})
#house.head()
houseinfo_split = pd.DataFrame((x.split('|') for x in house.houseinfo),index=house.index,columns=['xiaoqu','huxing','mianji','chaoxiang','zhuangxiu','dianti'])
#houseinfo_split.head()
house=pd.merge(house,houseinfo_split,right_index=True, left_index=True)
#house.head()
followinfo_split = pd.DataFrame((x.split('/') for x in house.followinfo),index=house.index,columns=['guanzhu','daikan','fabu'])
house=pd.merge(house,followinfo_split,right_index=True, left_index=True)
#house.head()
house=house.drop(['houseinfo','followinfo'],axis=1)
print "total collect"+str(len(house))+"houseinfomation"
house.head()