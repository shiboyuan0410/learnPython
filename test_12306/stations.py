# -*- coding:utf-8 -*-
import re
import urllib
from urllib import request

from pprint import pprint


def get_stations():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955'
    req = urllib.request.Request(url)
    r = urllib.request.urlopen(req).read().decode('utf-8')

    stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', r)  # 匹配中文和对应的英文
    stations = dict(stations)

    stations = dict(zip(stations.keys(), stations.values()))  # 将匹配的内容转化为字典
    #  pprint(stations)  # 以列的形式打印出来

    stations_ = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', r)  # 匹配中文和对应的英文
    stations_ = dict(stations_)
    stations_ = dict(zip(stations_.values(),stations_.keys()))  # 将匹配的内容转化为字典
    pprint(stations_)  # 以列的形式打印出来


'''
    获取地址信息 map
'''
if __name__ == "__main__":
    # 调用函数
    get_stations()
    print("爬取完毕！")
