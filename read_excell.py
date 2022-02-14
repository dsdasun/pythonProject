# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/9 13:59
@Auth ： 三水菇凉
"""
# import lib
import xlrd
class ReadExcel_Test:
    def __init__(self,file):
        '''读取excel文件'''
        self.file=file
        print(self.file)
        # file='D:/2.sanshui_file/Python_code/Datas/OA_Datas/【OA】报销申请（有发票）.xls'                                                #excel文件路径
        self.SheetName='OA-Data-Test'
        # print(SheetName,)#Test测试数据的表格名

    def data_file(self):
        if self.file.endswith(".xls"):  # 判断文件是否为Excel文件
            try:
                data = xlrd.open_workbook(self.file)  # 打开文件

                if type(self.SheetName) == int:  # 以下标的形式读取表格
                    table = data.sheet_by_index(self.SheetName)
                elif type(self.SheetName) == str:  # 以表格名的形式读取表格
                    table = data.sheet_by_name(self.SheetName)
                    nrows = table.nrows  # 获取总行数
                    ncols = table.ncols  # 获取总列数

                    keys = table.row_values(0)  # 获取第一行 列表格式
                    datalist=[]  # 存放所有测试用例
                    # 从1开始 不保存第一行
                    for i in range(1, nrows):
                        values = table.row_values(i)  # 依次获取每一行
                        # keys，values组合转换为字典
                        api_dict = dict(zip(keys, values))
                        datalist.append(api_dict)  # 添加到列表中
                    return datalist
            except Exception as e:
                print("[%s]用例获取失败,错误信息：%s" % (self.file, e))
        else:
            print("用例文件不合法:[%s]" % (self.file))



    @staticmethod
    def get_parameter01(data,n):
        return data[n].get('Case_figure')
        # return ReadExcel_Test.datalist[n].get('Case_figure')

    @staticmethod
    def get_parameter02(n):
        return ReadExcel_Test.datalist[n].get('Sponsor_yname')

    @staticmethod
    def get_parameter03(n):
        return ReadExcel_Test.datalist[n].get('Application_name')

    @staticmethod
    def get_parameter04(n):
        return ReadExcel_Test.datalist[n].get('Model_name')

    @staticmethod
    def get_parameter05(n):
        return ReadExcel_Test.datalist[n].get('Operator_Status_and_status')

    @staticmethod
    def get_parameter06(n):
        return ReadExcel_Test.datalist[n].get('png_if')

    @staticmethod
    def get_parameter07(n):
        return ReadExcel_Test.datalist[n].get('Node_Opeator_SpecialPerson')

    @staticmethod
    def get_parameter08(n):
        return ReadExcel_Test.datalist[n].get('additional_parameter')

    @staticmethod
    def get_parameter09(n):
        return ReadExcel_Test.datalist[n].get('modify_parameter')
#
# class ReadExcel_UAT:
#     '''读取excel文件'''
#     file='D:/2.sanshui_file/Python_code/Datas/OA_Datas/【OA】报销申请（有发票）.xls'                                                #excel文件路径
#     SheetName = 'OA-Data-UAT'                     # UAT测试数据的表格名
#
#     if file.endswith(".xls"): # 判断文件是否为Excel文件
#         try:
#             data = xlrd.open_workbook(file)       #打开文件
#             if type(SheetName) == int: #以下标的形式读取表格
#                 table = data.sheet_by_index(SheetName)
#             elif type(SheetName) == str: #以表格名的形式读取表格
#                 table = data.sheet_by_name(SheetName)
#                 nrows = table.nrows #获取总行数
#                 ncols = table.ncols #获取总列数
#
#                 keys = table.row_values(0) # 获取第一行 列表格式
#                 datalist = [] #存放所有测试用例
#                 # 从1开始 不保存第一行
#                 for i in range(1,nrows):
#                     values = table.row_values(i) #依次获取每一行
#                     # keys，values组合转换为字典
#                     api_dict=dict(zip(keys, values))
#                     datalist.append(api_dict) #添加到列表中
#                     # return datalist
#
#         except Exception as e:
#             print("[%s]用例获取失败,错误信息：%s" % (file, e))
#     else:
#         print("用例文件不合法:[%s]"%(file))
#
#     @staticmethod
#     def get_parameter01(n):
#         return ReadExcel_UAT.datalist[n].get('Case_figure')
#
#     @staticmethod
#     def get_parameter02(n):
#         return ReadExcel_UAT.datalist[n].get('Sponsor_yname')
#
#     @staticmethod
#     def get_parameter03(n):
#         return ReadExcel_UAT.datalist[n].get('Application_name')
#
#     @staticmethod
#     def get_parameter04(n):
#         return ReadExcel_UAT.datalist[n].get('Model_name')
#
#     @staticmethod
#     def get_parameter05(n):
#         return ReadExcel_UAT.datalist[n].get('Operator_Status_and_status')
#
#     @staticmethod
#     def get_parameter06(n):
#         return ReadExcel_UAT.datalist[n].get('png_if')
#
#     @staticmethod
#     def get_parameter07(n):
#         return ReadExcel_UAT.datalist[n].get('Node_Opeator_SpecialPerson')
#
#     @staticmethod
#     def get_parameter08(n):
#         return ReadExcel_UAT.datalist[n].get('additional_parameter')
#
#     @staticmethod
#     def get_parameter09(n):
#         return ReadExcel_UAT.datalist[n].get('modify_parameter')

# k=ReadExcel()
# print(k.datalist)