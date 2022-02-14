# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/9 13:59
@Auth ： 三水菇凉
"""

#第一题
#第一种
# a=10
# b=20
# if a>b:
#     print('a>b')
# elif a<b:
#     print('a<b')
# elif a==b:
#     print('a==b')
# elif a<=b:
#     print('a<=b')
# else:
#     print('数据类型错误')

# '''
# 字符串分割
# 用法: 字符串名[起始位置:结束位置:步长]
#
# '''
# s='长江大学专业姓名学号'
# print(s[2:6])
# print(s[4:])
# print(s[1::2])

# from unittest import mock
# # name定义了mock对象的唯一标示符
# testMock = mock.Mock(name='MyMock')
# print(testMock)

"""
构造器：参数spec
"""
from unittest import mock
# 指定属性组成的list
MyList = ['username','password']
# spec设置mock对象的属性，可以是property或者方法；属性可以是一个列表字符串或者是其他的Python类
testMock = mock.Mock(spec=MyList)
print(testMock)
print(testMock.username)
print(testMock.password)

