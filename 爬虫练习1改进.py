import requests
headers={"User-Agent":"Mozilla/5.0(Windows NT 10.0; Win64; x64)"}
response=requests.get("https://www.bilibili.com/"，headers=header)

if response.ok:
    print(response.text)
else:
    print("请求失败")
       

