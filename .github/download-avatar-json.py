import asyncio
import json

import requests

API_URL = "https://api.github.com/repos/DGP-Studio/Snap.Metadata/contents/Genshin/CHS/Avatar"

jsons=[]
# 发送请求获取文件列表
response = requests.get(API_URL)
files = response.json()
re=requests.get(files[0]['download_url'])
for file in files:
    re=requests.get(file['download_url'])
    jsons.append(re.json())

with open("./Avatar.json", 'w') as json_file:
    json.dump(jsons, json_file, indent=4)
