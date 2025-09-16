import requests
response=requests.get("https://www.bilibili.com/")
if response.ok:
    print(response.text)
else:
    print("请求失败")
       

