import requests
from bs4 import BeautifulSoup
import time

url="https://pic.netbian.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
}
resp=requests.get(url,headers=headers)
resp.encoding="gbk"
#print(resp.text)
time.sleep(2)
page=BeautifulSoup(resp.text,"html.parser")
#print(page)
alist=page.find('ul',attrs={'class':"clearfix"}).find_all("a")
#print(alist)


#imgsrc=[]
# for a in alist:
#     title=a.get('title')
#     #print(title)
#     src=a.find('img')['src']
#     #print(src)
#     imgsrc.append(title)
#     imgsrc.append(str(url)+str(src))
# print(imgsrc)
# resp.close()
# imgsrc=[]
imgsrc=dict()
for a in alist:
    title=a.get('title')
    #print(title)
    src=a.find('img')['src']
    #print(src)
    furl=str(url)+str(src)
    imgsrc[title]=furl
for key, value in imgsrc.items():
    print(f"{key}: {value}")
resp.close()