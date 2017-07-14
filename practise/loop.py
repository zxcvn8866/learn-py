#!usr/etc/env python3
#-*- coding:utf-8 -*-
names = ['Michael', 'Bob', 'Tracy']
for item in names:
    print(item)
#计算100以内所有奇数之和
sum = 0
for x in range(100):
	if x%2 != 0:
		sum = x+sum
print(sum)		
sum = 0 
num = 99
while num>0:
	if num%2 == 0:
		num=num-1
		continue
	sum = sum+num
	num = num-1
	if sum > 2000:
		break
print(sum)