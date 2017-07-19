#!usr/etc/env python3
# -*- coding:utf-8 -*-
# python 内置数据结构dict(字典 or assoc_array in php) key为不可变对象
# 快速查找，占用内存多浪费

score = {'zjj': 98, 'jxy': 100}
score['zjj'] = 139
# 获取字典中元素的值dict.get(item,default)
print(score.get('zjj'))
print(score.get('sq', 0))
print(score.get('sq'))
print(score['zjj'])
# 删除一个key
score.pop('jxy')
print(score)

# list 有序集合列表 可变 索引数组
# list 相关函数 len(list) list.pop() list.append(value) list.insert(index,value)

