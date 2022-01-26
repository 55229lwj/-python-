# bing词典
import requests
import re
import time
while True:
    url = "https://cn.bing.com/dict/search"
    word = input("想查的英文单词(按Q退出)")
    if word == "q":
        print("再见")
        break
    else:
        P = {
        "q": f"{word}"
        }
        resp = requests.get(url=url, params=P)
        goal = resp.text
        obj = re.compile(r'<meta name="description" content="(?P<meaning>.*?)" />')
        it = obj.search(goal)
        print(it.group("meaning"))
        resp.close()
        time.sleep(1)
