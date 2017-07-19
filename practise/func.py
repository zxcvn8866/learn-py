# !/usr/bin/env python 3.5
# -*- coding: utf-8 -*-

# 函数的运用

def circle(x):
    pi = 3.1415926
    return pi*x**2

def my_func(x, y):
    if x > y:
        return y
    else:
        return x

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x

# 函数参数的设定 位置参数、可变参数、默认参数(设为不可变对象)、关键字参数
# 位置参数 求x的n次方乘积
def dis(x, n):
    return x**n
# 默认参数 默认参数必须指向不变对象(str/None)
# 必选参数在前，默认参数在后
# 变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
def defau(name, score, age=6, city='bj'):
    return {'name': name, 'score': score, 'age': age, 'city': city}
# 可变参数 参数前加* 参数内部接收的是个tuple
def bian(*param):
    num = 0
    for x in param:
        num = x+num
    return num
l = [1, 2, 3]
print(bian(*l))
# 关键字参数





