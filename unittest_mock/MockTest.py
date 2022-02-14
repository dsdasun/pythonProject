"""
基本示例：测试类
"""
'''不使用mock'''
# import unittest
# from unittest_mock import Demo
#
# class TestDemo(unittest.TestCase):
#
#     def test_request(self):
#         print(Demo.send_request())
#         self.assertEqual(Demo.send_request(), 200)
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)

'''mock数据'''
'''
（1）首先实例化Mock类得到一个mock对象，并且设置这个mock对象的行为（返回值为404）。
（2）使用这个mock对象替换掉我们想替换的对象（Demo.get）。
（3）调用Demo.send_request()，期望和预设值一样（404）。
'''
import unittest
from unittest import mock
from unittest_mock import Demo

class TestDemo(unittest.TestCase):

    def test_request_mock(self):
        Demo.get = mock.Mock(return_value=404)
        print(Demo.get())
        self.assertEqual(Demo.send_request(),404)

if __name__ == '__main__':
    unittest.main(verbosity=2)