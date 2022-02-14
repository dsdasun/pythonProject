# # #函数中定义返回函数
# def hi(name="yasoob"):
#     def greet():
#         return "now you are in the greet() function"
#
#     def welcome():
#         return "now you are in the welcome() function"
#
#     if name == "yasoob":
#         return greet
#     else:
#         return welcome
#
# a = hi()
# print(a) #`a`现在指向到hi()函数中的greet()函数

#将函数作为参数传给另一个函数
# def hi():
#     return "hi yasoob!"
# def doSomethingBeforeHi(func):
#     print("I am doing some boring work before executing hi()")
#     print(func())
# doSomethingBeforeHi(hi)


# #函数装饰器
# def a(fun):
#     def b():
#         print('b1')
#         fun()
#         print('b2')
#     return b
#
# def c():
#     print('c')
#
# l=a(c)
# l()


# #简短的方式来生成一个被装饰的函数  @
# @a 相等于  c=a(c)
# def a(fun):
#     def b():
#         print('b1')
#         fun()
#         print('b2')
#     return b
# @a
# def c():
#     print('c')
# # c() #b1 c b2
# c=a(c)


# #如下代码会存在一个问题
# print(c.__name__)
#输出 b 这里被重写了函数的名字和注释文档

#解决方法
# from functools import wraps
# def a(fun):
#     @wraps(fun)
#     def b():
#         print('b1')
#         fun()
#         print('b2')
#     return b
# @a
# def c():
#     print('c')
# c() #b1 c b2
# c=a(c)
# print(c.__name__) #c

#装饰器的一些常用场景
#蓝本规范


'''
*args和**kwargs
多用在装饰器
# 当函数的参数不确定时，可以使用*args和**kwargs。
*args没有key值，**kwargs有key值
*args可以当作可容纳多个变量组成的list或tuple
'''
#无参数装饰器-包装有参函数
# from functools import wraps
# def logs(fun):
#     @wraps(fun)
#     def log(*args,**kwargs):  #接收传入的参数
#         print("打印日志")
#         sum=fun(*args,**kwargs) #使用传入的参数
#         print("值为",sum)
#     return log
#
# @logs
# def sum(x,y):
#     print(x,y)
#     return x+y
#
# sum(1,2)

#有参数装饰器-包装有参函数
# from functools import wraps
# def logs(name):
#     def decora(fun):
#         @wraps(fun)
#         def log(*args,**kwargs):  #接收传入的参数
#             print("打印日志")
#             print(f"日志名:"+name)
#             sum=fun(*args,**kwargs) #使用传入的参数
#             print("值为",sum)
#         return log
#     return decora
#
# @logs(name='测试')
# def sum(x,y):
#     print(x,y)
#     return x+y
#
# sum(1,2)


# 装饰器类的典型实现需要实现.__init__()和.__call__()：

# from functools import wraps
# class log(object):
#     def __init__(self,name):
#         self.name=name
#
#     def __call__(self, func):
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             tuple_args = args
#             dict_kwargs = kwargs
#             print(f"日志名："+self.name)
#             result=func(*args,**kwargs)
#             print("结果",result)
#             print(
#                 f'{func.__name__}(*args: tuple = {tuple_args}, **kwargs: dict = {dict_kwargs})')
#         return wrapper
#
# @log(name='测试')
# def sum():
#     x,y=1,2
#     return x+y
# sum()


'''
@timer装饰器开始。它将测量函数执行所需的时间并将持续时间打印到控制台
*args和**kwargs
多用在装饰器
# 当函数的参数不确定时，可以使用*args和**kwargs。
*args没有key值，**kwargs有key值
*args可以当作可容纳多个变量组成的list或tuple

在被装饰之后func.__name__返回的是装饰器内部函数wrapper
我们希望返回的是some_time本身
解决方式：装饰器应该使用@functools.wraps装饰器，它会保留有关原始函数的信息
'''
# import time
# from functools import wraps
#
# def timer(func):
#     @wraps(func)  #保留有关原始函数的信息
#     def wrapper(*args,**kwargs):
#         start_time=time.perf_counter()  #开始时间
#         value=func(*args,**kwargs)      #开始运行函数 有参函数需要使用*args,**kwargs 接收
#         end_time=time.perf_counter()    #结束时间
#         run_time=end_time-start_time    #总运行时长
#         print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
#         return value   #传递func()函数的返回值。如果不写，原有return则失效  装饰器会吃掉了函数的返回值返回none
#     return wrapper
#
# @timer
# def some_time(number):
#     sum=0
#     for i in range(number,100000):
#         sum=+i
#     return sum
#
# some_time(500)

# '''
# debugz装饰器:
#     在每次调用函数时打印调用函数的参数及其返回值
# repr() 函数将对象转化为供解释器读取的形式。
# '''
# from functools import wraps
#
# def debug(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         args_repr=[repr(a) for a in args]
#         kwargs_repr=[f"{k}={v!r}" for k,v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(f"Calling {func.__name__}({signature})")
#         value=func(*args,**kwargs)
#         print(f"{func.__name__!r} returned {value!r}")
#         return value
#     return wrapper
#
# @debug
# def make_greeting(name, age=None):
#     if age is None:
#         return f"Howdy {name}!"
#     else:
#         return f"Whoa {name}! {age} already, you are growing up!"
#
# make_greeting("Richard", age=112)


'''带参数的装饰器'''
from functools import wraps
def repeat(_func=None, *, num_times=2):
    #_func=None 判断装饰器是否传值
    def decorator_repeat(func):
        @wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    #判断装饰器是否被传递参数
    if _func is None:
        #没有传递直接调用
        return decorator_repeat
    else:
        #传递后使用传递后的参数
        return decorator_repeat(_func)


# @repeat(num_times=4) #传值
@repeat()#不传值
def greet(name):
    print(f"Hello {name}")

greet("World")

