'''
@File : reda_file.py 
@Time : 2021/12/10
@Author: sunda
@Software: PyCharm
'''
import csv
from datetime import datetime

def ReadCSV():
    '''读取csv文件'''
    file ='demo\AA00003.csv'
    if file.endswith(".csv"): #判断文件是否为csv文件
        try:
            csv_file = open(file, 'r', encoding='utf-8')
            datadict = csv.DictReader(csv_file)
            datalist = []
            for data in datadict:
                if datadict.line_num == 1:
                    continue
                else:
                    datalist.append(data)
            return datalist
        except Exception as e:
            print("[%s]用例获取失败,错误信息：%s"%(file,e))
    else:#如果不是csv文件则报错
        print("该用例文件不合法的，[%s]"% file)


def return_values(read_csv):

    select_data = []   #时间相差一个小时以上的，为常规经停记录
    select_data2 = []   #其他记录

    for i in range(len(read_csv) - 1):
        start_time = 0
        start_time = read_csv[i]['location_time']  # 开始时间
        end_time = read_csv[i + 1]['location_time']  # 结束时间
        print("前一条时间:{0}，后一条时间:{1}".format(start_time, end_time))
        result =(datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S") - datetime.strptime(start_time,"%Y-%m-%d %H:%M:%S")).total_seconds() #不同日期之间相隔多少时间差 结果为秒
        #print(result, type(result))
        # 判断时间间隔是否大于1小时
        if int(result) >= 3600:
            select_data.append(read_csv[i])
        else:
            select_data2.append(read_csv[i])

    print('select_data:', select_data)
    for j in select_data:
        print(j)
    print("常规经停记录一共有{0}条数据".format(len(select_data)))
    #print('select_data2:', select_data2)

    return select_data


values=return_values(ReadCSV())