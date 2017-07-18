#!usr/etc/env python3
# -*- coding:utf-8 -*-
#python 内置数据结构dict(字典 or assoc_array in php)
#快速查找，占用内存多浪费

score = {'zjj':98,'jxy':100}
score['zjj'] = 139
#获取字典中元素的值dict.get(itme,default)
print(score.get('zjj'))
print(score.get('sq', 0))
print(score.get('sq'))
print(score['zjj'])
#删除一个key
score.pop('jxy')
print(score)