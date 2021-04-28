import requests
from prettytable import PrettyTable
from color_set import colored
from station import stations , station_v
from get_urltrain import url


def query_tickes():

    r = requests.get(url, verify=False)  # 请求网址1的内容
    json_data = r.json()
    json_result = json_data['data']['result']


    trains = PrettyTable()
    trains.field_names = ["车次", "车站", "时间", "历时", "商务座", "一等座",
                          "二等座", "高级软卧", "硬卧 ", "软座 ", "硬座", "无座"]

    for row in json_result:  # 列表循环
        cells = row.split("|");
        trains.add_row([cells[3],
                        '\n'.join([colored('green', station_v[cells[6]]),
                                   colored('red', station_v[cells[7]])]),
                        '\n'.join([colored('green', cells[8]),  # 对于双行示的信息，设置颜色
                                   colored('red', cells[9])]),
                        cells[10],  # 历时
                        cells[31],  # 商务座 / 特等座
                        cells[30],  # 一等座
                        cells[29],  # 二等座
                        cells[25],  # 高级 / 软卧
                        cells[27],  # 硬卧 / 二等卧
                        cells[24],  # 软座
                        cells[28],  # 硬座
                        cells[26]])  # 无座

    print(trains)

    # print(json_result)


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    try:
        query_tickes()
    except Exception:
        print
        "爬取失败！"
        query_tickes()
    else:
        print
        "爬取完毕！"
