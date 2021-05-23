import requests
import os
url ="https://webfs.yun.kugou.com/202008181650/7164d14cc8b6839c6422c8cf6ba8e227/G182/M08/00/01/lpQEAF3qGNGAQ63lADDYqW5Mndk124.mp3"
headers ={"referer": "https://music.163.com/outchain/player?type=2&id=1352002513&auto=1&height=66&bg=e8e8e8",
"sec-fetch-dest": "audio",
"sec-fetch-mode": "no-cors",
"sec-fetch-site": "cross-site",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
response  = requests.get(url,headers=headers)
data = response.content
file = input("请输入要存放的文件目标")
with open(file,'wb') as f :
    f.write(data)
if os.path.exists(file) :
    print("爬取成功")
else:
    print("爬取失败")