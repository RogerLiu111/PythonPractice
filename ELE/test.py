from lxml import etree
import re

a = 'aaa.txt'

with open(a, "r", encoding='utf-8') as rawdata:
    text = rawdata.read()

# print(text)

# html = etree.HTML(text)
# section_list = html.xpath("//section[@class='shoplist']/section")
# for section in section_list:
#     '''
#     遍历店铺所有信息
#     '''
#     # 建立店铺字典
#     shop = {}
#
#     # 获取店铺名称
#     shop_name = section.xpath("./div/div[@class='index-main_N3FfcSz']/section/h3[@class='index-shopname_39Y7e3U']/span")
#     if len(shop_name):
#         name = shop_name[0].text.strip()
#         shop['店名'] = name
#
#     print(shop)
with open('abc.txt', 'a', encoding='utf-8') as hh:
    hh.write('')