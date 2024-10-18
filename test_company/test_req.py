# -*- codeing = utf-8 -*-
import requests

head = {  # 模拟浏览器头部信息，向服务器发送消息
    "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36",
    'Cookie': 'Hm_lvt_b58fe8237d8d72ce286e1dbd2fc8308c=1728964121,1728972478; HMACCOUNT=187252C21C2236C4; Hm_lpvt_b58fe8237d8d72ce286e1dbd2fc8308c=1728973010; C3VK=aad932',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}


# 获取接口返回信息
def askURL(url,payload):
    response = requests.request("POST", url, headers=head, data=payload)
    return response.text

# 下载单个图片
def dowmloadPdf(pdfUrl,rootPath,pdfName):
    # print(f'现在开始下载图片...{rootPath} {pdfName}')
    responsepdf = requests.get(pdfUrl, headers=head)

    # print(responsepdf.status_code)
    if responsepdf.status_code == 200:
        with open(r'' + rootPath + '/pdf/' + pdfName, "wb") as code:
            code.write(responsepdf.content)


# 批量下载图片
def dowmloadPdfList(pdfUrl,rootPath,datalist):
    print('现在开始下载图片...')
    for data in datalist:
        #print(data)
        pdfName = data[6]

        responsepdf = requests.get(pdfUrl, headers=head)

        print(responsepdf.status_code)
        if responsepdf.status_code == 200:
            with open(r'' + rootPath + '/pdf/' + pdfName, "wb") as code:
                code.write(responsepdf.content)
                #time.sleep(5)  # 防止访问速度过快，可以灵活的调整时间