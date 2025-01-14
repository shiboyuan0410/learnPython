#coding=utf-8
import requests
from bs4 import BeautifulSoup
import urllib.request, urllib.error  # 制定URL，获取网页数据
import re


# 创建正则表达式对象
findLink = re.compile(r'<a.*>(.*?)</a>', re.S)

def getData(bsobj):
    data = []  # 标题
    item = bsobj.find('ul', class_="def")
    for item_li in item.find_all('li'):  # 查找符合要求的字符串
        item_li = str(item_li)
        link = re.findall(findLink, item_li)  # 通过正则表达式查找
        print(link)
        #data.append(link)

    return data



# 得到指定一个URL的网页内容
def askURL(url):
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
    }
    # 用户代理，表示告诉服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def main():
    # resp=requests.get('https://www.csdn.net/') #请求csdn
    # print(resp.content)
    # bsobj = BeautifulSoup(resp.content, 'html.parser')  # 将网页源码构造成BeautifulSoup对象，方便操作

    html = askURL('https://www.csdn.net/')  # 保存获取到的网页源码
    bsobj=BeautifulSoup(html,'html.parser') #将网页源码构造成BeautifulSoup对象，方便操作

    dataList = getData(bsobj)

    for data in dataList:
        print(data)


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
     main()
     print("爬取完毕！")


