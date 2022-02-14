# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/13 16:59
@Auth ： 三水菇凉
"""
# import lib
from read_excell import ReadExcel_Test
import unittest

excel=ReadExcel_Test('C:/Users/v_vdasun/Downloads/1.xls')
data=excel.data_file()
print(excel.data_file())
excel.get_parameter01(data,0)
print(excel.get_parameter01(data,0))


# class LoginTest(unittest.TestCase):
#     def test_01(self):
#         pass



    # def test_02(self):
    #     OA_Flow(ReadExcel_Test.get_parameter01(1), ReadExcel_Test.get_parameter02(1),
    #             ReadExcel_Test.get_parameter03(1), ReadExcel_Test.get_parameter04(1),
    #             ReadExcel_Test.get_parameter05(1), ReadExcel_Test.get_parameter06(1),
    #             ReadExcel_Test.get_parameter07(1), ReadExcel_Test.get_parameter08(1),ReadExcel_Test.get_parameter09(0))

