# -*- codeing = utf-8 -*-
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配`
import urllib.request, urllib.error  # 制定URL，获取网页数据
import json



def main():
    baseurl = "https://cms-api.csdn.net/v1/web_home/select_content?componentIds=www-blog-recommend&cate1=java"  #要爬取的网页链接
    getData(baseurl)


# 解析json
def getData(baseurl):

    json_data = askURL(baseurl)  # 保存获取到的网页源码
    articles_str = json.loads(json_data)
    extends_data = articles_str["data"]["www-blog-recommend"]["info"]
    print(extends_data)
    for extend in extends_data:
        print(extend["extend"]["title"])


# 得到指定一个URL的网页内容
def askURL(url):
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
    }
    # 用户代理，表示告诉服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）
    request = urllib.request.Request(url, headers=head)
    json_data = ""
    try:
        response = urllib.request.urlopen(request)
        json_data = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return json_data


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
     main()
    # init_db("movietest.db")
     print("爬取完毕！")
