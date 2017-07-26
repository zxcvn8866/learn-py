# !/usr/bin/env python3.5
# -*- coding:utf-8 -*-

# 高阶函数 函数能接受函数作为参数传入，也能返回一个函数
def add(x,y,abs):
    return abs(x)+abs(y)
print(add(-9,1,abs))
import  math
def compute(xs=[],*fs):
    res = [f(x) for x in xs for f in fs]
    return res
print(compute([4.5],math.ceil,math.floor,abs))

# iterator =  map(fn,iterable) The same ad like array_map in PHP
# 将传入的函数依次作用到序列的每个元素上，并把结果作为新的iterator返回
# iterator 是惰性序列，所以需要list方法将整个序列都计算出来并返回个list
# 将运算规则抽象化
def f(x):
    return x**2
r = map(f,[1,2,3])
print(list(r))

# reduce The same as like array_reduce in PHP
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
def fn(x,y):
    return x*10+y
from functools import reduce
print(reduce(fn,[1,3,5,7,9]))

# 将str转int
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print(reduce(fn,map(char2num,'13479')))

name = ['zjj','LSADA','aLdfasd']
def up(unm):
    return unm.capitalize()
print(list(map(up,name)))

# 利用reduce求列表积
def prod(l):
    return reduce(lambda x,y:x*y,l)
print('3*5*7*9=',prod([3,5,7,9]))

# str2float '123.456'
def strtofloat(s):
    s1 = s.split('.')
    length = len(s1[1])
    return reduce(lambda x,y:x+y/int('1'+'0'*length),list(map(int,s1)))
print('strtofloat(\'123.456\')=',strtofloat('123.456'))

# filter函数 用于过滤序列 The same as like array_filter() in PHP
# filter()也接收一个函数和一个序列
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素


