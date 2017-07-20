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
# 关键字参数 **kw 参数内部接受的是个字典{},可以传入0个，1个或者多个kv结构的参数
def person(name, age, **kw):
    return name, age, kw
d = {'sex': '男', 'city': 'HD'}
print(person('zjj', 27, **d))
print(person('zjj', 27, sex='男', city='HD'))
# 命名关键字参数 只可以使用命名的关键字作为关键字参数传入函数
# 如果由可变参数*param,就不用加分隔符*，否则需要加分隔符
# 如不加分隔符，则关键字参数被python视为位置参数，会报错，因为python函数只可以接受2个位置参数
# 命名关键字参数如果无缺省值就必须都传入，有默认值则可不传
def person(name, age, *, city='BJ', job='engineer'):
    return name, age, city, job
print(person('zjj', 98, job='phper'))
# 参数组合 5种参数都可以组合使用
# 但是参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 另一种方式对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
# *args是可变参数，args接收的是一个tuple；**kw是关键字参数，kw接收的是一个dict。
def person(name, age, city='BJ', *args, **kw):
    return name, age, city, args, kw
t = ('zjj', 27)
l = ['zjj', 28]
d = {'sex': '男', 'job': 'PHPer'}
print(person(*l, 'HD', *t, **d))
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，
# 再通过*args传入：func(*(1, 2, 3))；

# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，
# 再通过**kw传入：func(**{'a': 1, 'b': 2})。





