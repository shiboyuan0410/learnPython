import re
import requests
import os

re_pic_url = re.compile(r'"objURL":"(.*?)"')
rootPath = os.getcwd()
countNum = 0


def dowmloadPic(html, keyword):
    global countNum  # global声明

    html = str(html)
    pic_url = re.findall(re_pic_url, html)

    print('找到关键词:' + keyword + '的图片，现在开始下载图片...')

    for each in pic_url:
        print('正在下载第' + str(countNum) + '张图片，图片地址:' + str(each))
        try:
            pic = requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue

        dir = r'' + rootPath + '/images/i' + keyword + '_' + str(countNum) + '.jpg'
        #dir = r'D:/images/i' + keyword + '_' + str(abc) + '.jpg'
        if not os.path.exists(rootPath + '/images'):
            os.makedirs(rootPath + '/images')

        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        countNum += 1

#根据关键词从百度下载 图片
if __name__ == "__main__":  # 当程序执行时

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
    name = "鲜花"
    num = 0
    pn = 2

    countNum = 1

    for i in range(int(pn)):

        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + name + '+&pn=' + str(i*20)
        print(url)
        result = requests.get(url, headers=headers)
        dowmloadPic(result.content, name)

    print("爬取完毕！")
