'''
    本程序使用方法
    1.首先将饿了么网页版的数据处理一下
        1）定位需要获取竞队信息的地点
        2）打开店铺列表目录
        3）复制列表信息到目录下的"raw data.txt"文档中，如果没有此文档，请新建
    2.运行程序
    3.在程序目录中寻找输出的TXT文档
'''

from lxml import etree
import re

# 输入网页源码
inputRawData = 'aaa.txt'
# 输出获取数据
outputData = 'aaa_E.txt'


# 建立店铺列表
shops = []

# 读取已经在网页上复制下来的源码文件
with open(inputRawData, "r", encoding='utf-8') as rawdata:
    text = rawdata.read()

# 制作xpath路径
html = etree.HTML(text)
section_list = html.xpath("//section[@class='shoplist']/section")
for section in section_list:
    '''
    遍历店铺所有信息
    '''
    # 建立店铺字典
    shop = {}

    # 获取店铺名称
    shop_name = section.xpath("./div/div[@class='index-main_N3FfcSz']/section/h3[@class='index-shopname_39Y7e3U']/span")
    if len(shop_name):
        name = shop_name[0].text.strip()
        shop['店名'] = name

    # 获取店铺单量
    shop_orderNum = section.xpath("./div/div[@class='index-main_N3FfcSz']/section/div[@class='index-rateWrap_39dWx_g']/span[2]")
    if len(shop_orderNum):
        orderNum = shop_orderNum[0].text.strip()
        num = r"\d+"
        pattern = re.compile(num)
        orderNum = pattern.match(orderNum,2,10)
        orderNum = orderNum.group()
        shop['单量'] = orderNum

    # 获取店铺评分
    shop_score = section.xpath("./div/div[@class='index-main_N3FfcSz']/section/div[@class='index-rateWrap_39dWx_g']/span[@class='index-rate_WsK58g8']")
    if len(shop_score):
        score = shop_score[0].text.strip()
        shop['店铺评分'] = score

    # 获取店铺距离
    shop_distanse = section.xpath("./div/div[@class='index-main_N3FfcSz']/section/div[@class='index-timedistanceWrap_2Dp_kzY']/span[@class='index-distanceWrap_1EPAlti']")
    if len(shop_distanse):
        distanse = shop_distanse[0].text.strip()
        shop['距离'] = distanse

    # 获取店铺配送费用
    shop_freight = section.xpath("./div/div[@class='index-main_N3FfcSz']/section/div[@class='index-moneylimit_2fCq9W5']/span[2]")
    if len(shop_freight):
        freight = shop_freight[0].text.strip()
        shop['配送费'] = freight

    # 获取店铺满减活动
    shop_discount = section.xpath("./div/section[@class='index-activities_25AUDsx']/div[@class='index-activityList_1wvwwUY']/div[@class='index-actRow_2f_uNNA']/span[@class='index-desc_JLha7Vr']")
    if len(shop_discount):
        discount = shop_discount[0].text.strip()
        shop['满减力度'] = discount

    if shop != {}:
        shops.append(shop)

# 店铺序号
i = 0
for single in shops:
    with open(outputData, "a", encoding='utf-8') as shop_data:
        i = i + 1
        a = str(i)
        shop_data.write("销量排名: ")
        shop_data.write(a)
        shop_data.write("\n")
    for head in single:
        with open(outputData, "a", encoding='utf-8') as shop_data:
            shop_data.write(head)
            shop_data.write(": ")
            shop_data.write(single[head])
            shop_data.write("\n")
    with open(outputData, "a", encoding='utf-8') as shop_data:
        shop_data.write("\n")
# with open("ELE DATA GET TEST", "a", encoding='utf-8') as shop_data:
#     f.write(shop_data)