from station import stations
import warnings

# f1 = input('请输入起始城市：\n')
f1 = '北京'
f = stations[f1]

# t1 = input('请输入目的城市：\n')
t1 = '邢台'
t = stations[t1]

# d1 = input('请输入出发时间： \n')
d1 = '2020-04-30'
d = str('2021-') + str(d1)  # 这里讲年份设置为固定值，可以减少输入操作。

print('正在查询' + f1 + '至' + t1 + '的列车，请听听音乐...')  # 个性旁白

url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2021-04-30&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=XTP&purpose_codes=ADULT'
warnings.filterwarnings("ignore")  # 这个网站是有安全警告的，这段代码可以忽略警告</span></span>
