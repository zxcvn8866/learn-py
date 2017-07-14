#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#条件判断
age = int(input('please enter your age:'))
if age<=3:
	print('kids')
elif age>3 and age<12:
	print('teenager')
else:
	print('adults')

s = float(input('enter your heigth(m):')) 
h = float(input('enter your weigth(kg):')) 
BMI = h/s**2 
if BMI<=18.5: 
	print('your BMI:%.1f' %BMI,'过轻') 
elif BMI<=25: 
	print('your BMI:%.1f' %BMI,'正常') 
elif BMI<=28: 
	print('your BMI:%.1f' %BMI,'过重') 
elif BMI<=32: 
	print('your BMI:%.1f' %BMI,'肥胖') 
else: 
	print('your BMI:%.1f' %BMI,'严重肥胖')	