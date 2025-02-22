from DrissionPage import Chromium, ChromiumPage
import pandas as pd


dp = ChromiumPage()
dp.listen.start("json/fetchHotelList")
dp.get("https://hotels.ctrip.com/hotels/list?countryId=1&city=17&optionId=17&optionType=City&display=%E6%9D%AD%E5%B7%9E")

all_hotel_data = []
for page in range(1,5):
    print("正在打印第"+str(page)+"页")
    resp=dp.listen.wait()
    json_data=resp.response.body
    hotelList=json_data["data"]["hotelList"]

    # a=hotelList[1]["hotelInfo"]["nameInfo"]["name"]
    # print(a)

    #两种写法
    # 1
    # for index in range(len(hotelList)):
    #     print(index)
    #     hotel_name = hotelList[index]["hotelInfo"]["nameInfo"]["name"]
    #     print(hotel_name)
    # 2
    # hotel_name = index["hotelInfo"]["nameInfo"]["name"]
    # print(hotel_name)


    for index in hotelList:
        hotel_data = []
        dit={
            "酒店名":index["hotelInfo"]["nameInfo"]["name"],
            "星级": index["hotelInfo"]["hotelStar"]["star"],
            "地区":index["hotelInfo"]["positionInfo"]['cityName'],
            "地址":index["hotelInfo"]["positionInfo"]["address"],
            "总评分":index["hotelInfo"]["commentInfo"]["commentScore"],
            "环境评分": index["hotelInfo"]["commentInfo"]["subScore"][0]["number"],
            "卫生评分": index["hotelInfo"]["commentInfo"]["subScore"][1]["number"],
            "服务评分": index["hotelInfo"]["commentInfo"]["subScore"][2]["number"],
            "设施评分": index["hotelInfo"]["commentInfo"]["subScore"][3]["number"],
            "评论数":index["hotelInfo"]["commentInfo"]["commenterNumber"],
            #"一句话点评": index["hotelInfo"]["commentInfo"]["oneSentenceComment"][0]['tagTitle'],
            "价格":index["roomInfo"][0]["priceInfo"]["displayPrice"],
            }
        hotel_data.append(dit)  # 将当前酒店信息添加到列表中
        print(dit)
        all_hotel_data.extend(hotel_data)
        dp.scroll.to_bottom()
# 创建DataFrame并保存到Excel
df = pd.DataFrame(all_hotel_data)
df.to_excel('酒店信息.xlsx', index=False)

