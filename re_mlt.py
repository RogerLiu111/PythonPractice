'''
安装lxml
'''
from lxml import etree

'''
用lxml来解析HTML代码
'''
comments = []
pf_num = '9'
# text = ''' '''
with open(r'webdata.txt', encoding = 'utf-8') as f:
    text = f.read()

# print(text)
# 利用etree.HTML把字符串解析成HTML文档，格式化代码，补全，修正
html = etree.HTML(text)
rst = html.xpath("//div[contains(@class,'comment-block-3ul4F')]")

for r in rst:
    comment = {}

    pf = r.xpath("./div/span[contains(@class,'comment-block-kvT3T')]")
    if len(pf):
        star = pf[0].text.strip()
        if star == '超赞':
            pf_num = '5'
        if star == '满意':
            pf_num = '4'
        if star == '一般':
            pf_num = '3'
        if star == '较差':
            pf_num = '2'
        if star == '吐槽':
            pf_num = '1'
        comment['star'] = pf_num
    else:
        comment['customer'] = 'None'

    pl = r.xpath("./div[contains(@class,'comment-block-af0_9')]")
    if len(pl):
        customer = pl[0].text.strip()
        comment['customer'] = customer
    else:
        comment['customer'] = 'None'

    hf = r.xpath("./div[contains(@class,'comment-block-2h-Hq')]")
    if len(hf):
        business = hf[0].text.strip()
        comment['business'] = business
    else:
        comment['business'] = 'None'
    # print(business)

    print(comment)
    if comment != {}:
        comments.append(comment)

num = 0
for str in comments:
    num = num + 1
    strnum = '%d' % num
    with open(r'差评.txt', 'a') as f:
        f.write(strnum + '\n')
    for eve in str:
        with open(r'差评.txt','a',encoding = 'utf-8') as f:
            f.writelines(eve + ": " + str[eve] + '\n')
    with open(r'差评.txt', 'a') as f:
        f.write('\n')