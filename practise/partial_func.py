# !/usr/bin/env python3.5
# -*- coding:utf-8 -*-
from functools import partial
# 偏函数 依赖于functools模块的partial 方法 创建一个新的函数
int2 = partial(int,base=10)
print(int2('123'),int2('111',base=2))
