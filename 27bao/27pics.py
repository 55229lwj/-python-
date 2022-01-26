# 1.图片
import requests
import re
import time
i = eval(input("起始页"))
for i in range(20):
    i = i + 1
    url = f"https://www.27baobao.com/a/{i}.html"
    reps = requests.get(url=url)
    goal = reps.text
    obj = re.compile(r'<img alt=".*?" referrerPolicy="no-referrer" src="(?P<pic>.*?)" />')
    it = obj.search(goal)
    img_src = it.group("pic")
    img = requests.get(img_src)
    n = i
    f = open(f"imgs/{n}.jpeg", "wb")
    f.write(img.content)
    reps.close()
    f.close()
    print(i, "is done")
    time.sleep(1)
print("all done")
