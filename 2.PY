import requests

# 设置请求头，模拟浏览器访问
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    # 发送GET请求
    response = requests.get("https://www.bilibili.com/", headers=headers)
    
    # 检查请求是否成功
    if response.ok:
        print("请求成功，页面内容如下：")
        print(response.text)
    else:
        print(f"请求失败，状态码：{response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"请求发生错误：{e}")