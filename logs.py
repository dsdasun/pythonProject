'''
@File : logs.py
@Time : 2021/4/29
@Author: sunda
@Software: PyCharm
'''
import logging
import time
import os
from functools import wraps
file_dir=os.path.dirname(__file__) #获取当前工作空间

class Log:
    def __init__(self,logname):
        self.logname=logname
        self.logger = logging.getLogger(self.logname)  #设置日志文件名
        self.logger.setLevel(logging.DEBUG)
        #存放日志文件的位置
        logpath = os.path.join(file_dir, 'logs/')
        self.handler = time.strftime('%Y_%m_%d_%H_%M_%S')
        self.logname = self.handler+'.txt'
        # 创建一个handler，用于写入日志文件 logging.FileHandler 用于向一个文件输出日志信息
        fh =logging.FileHandler(logpath+self.logname)
        # 默认日志的级别
        fh.setLevel(logging.INFO)
        # 设置日志的输出格式 # 定义handler的输出格式formatter
        formatter = logging.Formatter('%(asctime)s '
                              '- %(name)s'
                              '-%(levelname)s '
                              '- %(message)s')
        fh.setFormatter(formatter)
        # 给logger添加handler  将日志输出的信息添加到日志收集器中
        self.logger.addHandler(fh)

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            tuple_args = args
            dict_kwargs = kwargs
            result=func(*args,**kwargs)
        return wrapper
