import requests
import re
import csv
url = 'https://movie.douban.com/top250'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
}

resp = requests.get(url, headers=headers)
page_content=resp.text
#解析数据
obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
               r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
               r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
               r'<span>(?P<number>.*?)</span>'
               ,re.S)
result=obj.finditer(page_content)
# for i in result:
#     print(i.group("name"))
#     print(i.group("year").strip())
#     print(i.group("score"))
#     print(i.group("number"))

# 写入CSV文件
fieldnames = ['name', 'year', 'score', 'number']
with open("data.csv", mode="w", encoding='utf-8', newline='') as f:
    csvwriter = csv.DictWriter(f, fieldnames=fieldnames)
    csvwriter.writeheader()  # 写入头部
    for i in result:
        dic = i.groupdict()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic)

print("数据已写入CSV文件。")
resp.close()