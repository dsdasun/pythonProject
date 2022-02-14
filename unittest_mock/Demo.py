"""
基本示例：被测试函数
"""
# 引入Requests库
import requests

def get(url):
    # 发起GET请求
    r = requests.get(url)
    # 返回状态码
    return r.status_code

def send_request():
    # 调用get()函数
    return get('https://www.baidu.com/')