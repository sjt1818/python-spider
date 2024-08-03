import requests
import re
import csv

# 字段名
fieldnames = ['name', 'year', 'score', 'number']

# 打开CSV文件以写入，确保在循环外部进行
with open("data1.csv", mode="w", encoding='utf-8', newline='') as f:
    csvwriter = csv.DictWriter(f, fieldnames=fieldnames)
    csvwriter.writeheader()  # 写入头部

    # 遍历所有需要的页面
    for i in range(0, 251, 25):
        num = i
        url = f'https://movie.douban.com/top250?start={num}&filter='

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
        }

        resp = requests.get(url, headers=headers)
        page_content = resp.text

        # 解析数据
        obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                         r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
                         r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                         r'<span>(?P<number>.*?)</span>', re.S)
        result = obj.finditer(page_content)

        # 写入CSV文件
        for match in result:
            dic = match.groupdict()
            dic['year'] = dic['year'].strip()  # 去除年份前后的空白字符
            csvwriter.writerow(dic)

    print("所有数据已写入CSV文件。")

# 注意：这里不需要手动关闭resp，因为它会在离开with块时自动关闭（但在这个例子中，我们实际上没有使用with块来管理resp）
# 由于resp是局部变量，并且在每次迭代结束时都会被新的请求响应覆盖，所以Python的垃圾回收机制会处理它