#!/usr/bin/python3 
#coding=utf-8

# Python 中单行注释以 # 开头
print('Hello World!')

# 多行注释用三个单引号（'''）或者三个双引号（"""）将需要注释的内容囊括起来

a = -50
if a >= 0:
    print(a)
else:
    print(-a)

print('I\'m learning\nPython.')

 
'''
函数的测试用例
字符串格式化测试用例
'''
Money = 2000
def AddMoney():
   global Money
   Money = Money + 1
 
print(Money)
AddMoney()
print(Money)

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)