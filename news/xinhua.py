import requests
from lxml import etree
import pymysql  # 提交数据库用
import time
url = "http://xinhuanet.com"
resp = requests.get(url)
html = resp.text.encode('raw_unicode_escape').decode()
connect = pymysql.Connect(     # 连接数据库
    host='host',
    port=3306,
    user='root',
    passwd='your password',
    db='db',
    charset='utf8'
)
cursor = connect.cursor()
tree = etree.HTML(html)
top = tree.xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/div/div[@class="tit"]')   # 解析
for divs in top:        # 持久化
    news = divs.xpath('./a/text()')[0]
    urls = divs.xpath('./a/@href')[0]  # /html/body/div[10]/div/div/div[2]/div/div[2]/div[1]/div[1]/a
    print(news, urls)
    now_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    sql = f"INSERT INTO xhnews(times, xnews, url) VALUES('{now_time}', '{news}', '{urls}') "
    try:
        cursor.execute(sql)
    except Exception as e:
        connect.rollback()
        print("失败", e)
    else:
        connect.commit()
        print("数据库添加", cursor.rowcount, "条数据。")
print("all done")
cursor.close()
connect.close()
resp.close()
input("按任意键退出")
