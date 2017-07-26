# !/usr/bin/env python3.5
# -*- coding:utf-8 -*-

# 高级特性 代码越简单，执行效率越高 一行代码能解决的问题绝不用五行代码来解决
l = []
n = 1

while n <= 99:
    l.append(n)
    n = n+2
print(l)
# the same as like this
print(list(range(1, 100, 2)))

# slice 切片操作符 L[s:e]代表取L中从索引s到索引n的元素，不包括n,s为0时可省略
# 正切片 L[:10] 倒切片 L[-10:]
# 支持切片操作符的数据对象有list、tuple、str,切片后返回对应的数据结构
print(l[3:10], l[0:5], l[:5], l[-10:-1:2], l[:], l[::5], l[:-1:2], sep='\n')
l = list(range(0, 100))
# slice L[s:e:n] s:开始索引 e:结束索引 n:步数，正负代表方向，有相对应的s和e的缺省值
print(l[80::5], l[80::-5], sep='\n')

# iteration 迭代
l = {'name': 'zjj', 'age': 28, 'sex': 1}
# 迭代 value
for value in l.values():
    print(value)
# 迭代 key
for key in l:
    print(key, ':', l[key])
# 迭代k,v
for k, v in l.items():
    print(k, v, sep=':')
# enumerate 将可迭代的对象转换为一个索引序列，支持第二参数(设置初始索引，默认为0)
# 为python内置函数，返回enumerate对象
l = ['abc', 1, 13]
for k, v in enumerate(l):
    print(k, v, sep=':')


# 判断一个对象是否可迭代
def judge(x):
    from collections import Iterable
    return isinstance(x, Iterable)


c = ['abc', 123, [1, 2, 3], (1, 2, 3), set([1, 2, 3])]
# 对list中的每个元素执行相同操作
d = [judge(v) for v in c]
print(d)

# for循环同时引用两个变量 x,y=(1,2) x,y,z=(1,2,3)
# python的解构赋值 把一个tuple赋给多个变量
for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x, y)

# 列表生成式 python内置的list comprehensions
l = list(range(1,11))
l = [x*x for x in range(1,11)]
l = [x*x for x in range(1,11) if x % 2 == 0]
# 应用双层循环生成全排列
l = [m+n for m in 'ABC' for n in 'XYZ']

# 列出当前文件下的所有文件和目录名
import os
print([d for d in os.listdir('.')])

# for 循环同时使用多个变量 比如dict的items可以同时迭代key和value
# 使用两个变量来生成list
d = {'x':'A','y':'B','z':'C'}
l = [k+'='+v for k,v in d.items()]

# 将list的所有字符串变成小写
L = ['Apple','Bank','City','Down','Edit']
L = [s.lower() for s in L]
print(L)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)

# 生成器 generator 一边循环一边推算后续元素
# 定义  1. 将列表生成式的[]改成() []返回list object; ()返回generator object
# 2.通过函数内部加yield关键字实现复杂逻辑的generator
g = (x*x for x in range(10))

# 循环generator 属于可迭代对象 保存的是算法
for n in g:
    print(n)
# 著名的裴波拉契数列 除第一个和最后一个数外 任意一个数都可由前两个数相加得到
def fib(max):
    n,a, b = 0,0,1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
# fib(max) 函数内部加上yield 变成generator对象
for x in fib(6):
    print(x)
# 杨辉三角
def triangles(max):
    y = [1]
    n = 0
    while n < max:
        yield y
        n = n+1
        y.append(0)
        y = [y[i-1]+y[i] for i in range(len(y))]
for l in triangles(10):
    print(l)
# 迭代器 Iterator,可迭代对象 Iterable,迭代方法 iter()
def check(x):
    from collections import Iterator,Iterable
    return isinstance(x,Iterable) or isinstance(x, Iterator)

data = ['abc',123,['zjj','sq'],{'name':'zjj','sex':0},(1,2,3),set([1,2,3])]
res = [check(x) for x in data]
print(res)

arr = iter([1,2,3])
while True:
    try:
        x = next(arr)
        print(x)
    except StopIteration:
        break

