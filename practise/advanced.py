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


