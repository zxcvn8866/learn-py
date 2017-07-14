#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#python3内置有序集合list

#定义list
stu = ['zjj','sq','ly'];
#末尾追加
stu.append('end')
#向指定位置插入元素 require two arguments
stu.insert(0,'start')
#可以按kv直接替换
stu[1] = 'first'
#删除末尾元素
stu.pop()
#删除指定元素
stu.pop(1)
print(stu)
