from urllib.request import urlopen
url = "https://www.baidu.com"
resp=urlopen(url)
#print(resp.read().decode('utf-8'))
with open("mybaidu.html",mode='w',encoding='utf-8')as f:
    f.write(resp.read().decode('utf-8'))
print('over')