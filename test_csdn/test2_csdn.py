#coding=utf-8
import requests
from bs4 import BeautifulSoup
import re


# 创建正则表达式对象
findLink = re.compile(r'<a.*>(.*?)</a>', re.S)

def getData(bsobj):
    data = []  # 标题
    item = bsobj.find('ul', class_="nav_center_wrap")
    for item_li in item.find_all('li'):  # 查找符合要求的字符串
        item_li = str(item_li)
        link = re.findall(findLink, item_li)  # 通过正则表达式查找
        print(link)
        #data.append(link)

    return data

def main():
    resp=requests.get('https://www.csdn.net/') #请求csdn
    bsobj=BeautifulSoup(resp.content,'html.parser') #将网页源码构造成BeautifulSoup对象，方便操作
    dataList = getData(bsobj)

    for data in dataList:
        print(data)


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
     main()
     print("爬取完毕！")


