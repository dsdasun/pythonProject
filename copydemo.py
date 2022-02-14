import copy
'''
深拷贝浅拷贝
'''

a=[1,2,3,4,['a','b']]  #原始对象

b=a  #赋值，传对象的引用
c=copy.copy(a)  #对象拷贝，浅拷贝
d=copy.deepcopy(a) ##对象拷贝，深拷贝


a.append(5)  #修改对象a
a[4].append('c')   #修改对象a中的数组

print(f'a=',a)  #a= [1, 2, 3, 4, ['a', 'b', 'c'], 5]
print(f'b=',b)  #b= [1, 2, 3, 4, ['a', 'b', 'c'], 5]
print(f'c=',c)  #c= [1, 2, 3, 4, ['a', 'b', 'c']]
print(f'd=',d)  #d= [1, 2, 3, 4, ['a', 'b']]

