import requests
from lxml import etree
import pymysql
import time
url = "http://xinhuanet.com"
resp = requests.get(url)
html = resp.text.encode('raw_unicode_escape').decode()
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='lab',
    charset='utf8'
)
cursor = connect.cursor()
tree = etree.HTML(html)
top = tree.xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/div/div[@class="tit"]')
for divs in top:
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
