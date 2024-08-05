import requests
from bs4 import BeautifulSoup
url="http://www.vegnet.com.cn/Price/list_ar330000.html?marketID=72"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
}
resp=requests.get(url,headers=headers)
#print(resp.text)


#把页面源代码交给beautifulsoup处理，生成bs对象
page=BeautifulSoup(resp.text,"html.parser")
#从bs对象中查找数据
#1.find(标签，属性=值) 找第一个
#find_all(标签，属性=值) 找全部

#shucai=page.find_all('span',class_="k_2")
shucai=page.find_all('span',attrs={'class':"k_2"})
#print(shucai)

prices = []
product_names = []
for name in page.find_all('span', class_='k_2'):
    if name.text.startswith('¥'):  # 检查是否以'¥'开头，以确定这是价格
        prices.append(name.text)
    elif name.text not in ['元/千克(kg) ', '查找']:  # 排除非商品名和价格的文本
        product_names.append(name.text)

    # 由于价格和商品名在列表中可能不是一一对应的，我们可能需要通过索引来匹配它们
# 但这里我们假设每个商品名后紧跟着三个价格（虽然你的例子中有些价格为0）
for i in range(0, len(product_names), 1):
    try:
        product_name = product_names[i]
        current_price = prices[i * 3 + 2]  # 假设第三个价格是当前价格（忽略前两个可能为0的价格）
        print(f"{product_name}的价格是：{current_price}")
    except IndexError:
        # 处理索引超出范围的情况
        break

resp.close()