# !/usr/bin/env python3.5
# -*- coding:utf-8 -*-

# 面向对象编程 类和实例
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def echo(self):
        print('%s的成绩是:%s' % (self.__name,self.__score))

    def test(self,*args,**kw):
        print(type(args),type(kw))

    def get_score(self):
        print(self.__score)

    def set_score(self,score):
        if 0 < score <= 100:
            self.__score = score
        else:
            raise ValueError('bad param')
class Boy(Student):
    def echo(self):
        self.get_score()
        print(isinstance(self,Student))
zjj = Boy('zjj',98)
zjj.echo()
zjj.test('lalla')
zjj.set_score(100)
zjj.get_score()
# 获取对象信息
print(type(111) == int)  # true
isinstance('111',str)  # true
isinstance('1111',(list,tuple,str))  # true
type('111')  # class <str>
dir(str)  # 获取str对象的属性和方法
hasattr(str,'replace')  # true 查看str对象是否有replace方法
getattr(str,'name','zjj')  # 'zjj' 查看str对象是否有name属性 如没有默认为‘zjj’
getattr(str,'__len__')('111')  # 3  the sane as len('111')
setattr(zjj,'name','zjj')
print([getattr(zjj,i) for i in dir(zjj) if i == 'name'])  # zjj









