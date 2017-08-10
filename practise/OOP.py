# !/usr/bin/env python3.5
# -*- coding:utf-8 -*-

# 面向对象编程 类和实例
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def echo(self):
        print('%s的成绩是:%s' % (self.name,self.score))

    def test(self,*args,**kw):
        print(type(args),type(kw))

zjj = Student('zjj',98)
zjj.echo()
zjj.test('lalla')


