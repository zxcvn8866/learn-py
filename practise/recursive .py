# !/usr/bin/env python3.5
# -*- coding:utf-8 -*-

# 递归函数 在函数内部调用自身的函数
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)
print(fact(3))

# 汉诺塔算法 n:盘子的个数 a:起点 b:缓冲区 c:终点
def hanor(n, a, b, c):
    if n == 1:
        print('move', a+'-->'+c)
    else:
        hanor(n-1, a, c, b)  # 将n-1个盘子从a移动到b上
        hanor(1, a, b, c)  # 将最底下的1个盘子从a移动到c上
        hanor(n-1, b, a, c)  # 将n-1个盘子从b移动到c上
print(hanor(5, 'A', 'B', 'C'))
