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
# generator 属于惰性序列 不会一次性计算出所有序列元素的值，会通过next(i)来逐一取值
# 无限的奇数序列
def __odd__iter():
    n = 1
    while True:
        n = n + 2
        yield n

def primes():
    yield 2
    n = 2
    it = __odd__iter()
    while n < 1000:
        n = next(it)
        yield n
        it = filter(lambda x:x % n > 0,it)

print(list(primes()))

# 过滤掉1-1000范围内的回数如909
l = filter(lambda x:str(x) != str(x)[::-1],range(1,1000))
print(list(l))
# list = sorted(iterable,[key=func],[reverse=True]) 排序算法
l = [('Herb',87),('Bad',99),('Ada',89),('Bart',98)]
l1 = sorted(l,key=lambda x:x[0])
print(sorted(l1,key=lambda x:x[1],reverse=True))

# 返回函数 闭包函数是
def count():
    fs = []
    for i in range(1,4):
        fs.append(lambda j=i:j*j)
    return fs
print([print(i()) for i in count()])

# 匿名函数 作为函数返回值 冒号前是函数传入的参数 冒号后是个表达式作为匿名函数的返回值
def build(x,y):
    return lambda:x**2+y**2
print(build(2,3)())

# 装饰器  Decorator
def log(func):
    def wraper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wraper
@log
def now():
    import time
    print(time.clock())
now()

import functools
def log(*args):
    text = args[0] if isinstance(args[0],str) else 'log'

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s before %s():' % (text, func.__name__))
            result = func(*args, **kw)
            print('%s after %s():' % (text, func.__name__))
            return result
        return wrapper
    return decorator if isinstance(args[0],str) else decorator(args[0])
# 直接是修饰方法 相当于log(fn)
@log
def test1():
    print('test1')
test1()


# log('custom') 方法的返回值才是修饰方法 相当于log(str)(fn)
@log('custom')
def test2():
    print('test2')
test2()

