import asyncio
import json

import httpx
API_URL = "https://api.github.com/repos/DGP-Studio/Snap.Metadata/contents/Genshin/CHS/Avatar"

jsons=[]
# 发送请求获取文件列表
response = httpx.get(API_URL)
files = response.json()
async def fetch_data():
    async with httpx.AsyncClient() as client:
        for file in files:
            re=await client.get(file['download_url'])
            jsons.append(re.json())

asyncio.run(fetch_data())
with open("./Avatar.json", 'w') as json_file:
    json.dump(jsons, json_file, indent=4)
