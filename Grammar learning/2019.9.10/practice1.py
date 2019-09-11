"""
输入一个正整数判断它是不是素数

Version: 0.1
题目作者: 骆昊
程序作者: Sep
出题: 2018-03-01
"""
from math import sqrt

x = int(input("输入一个正整数："))
end = sqrt(x) + 1
a = 2
if x == 1:
    print("1既不是一个素数也不是一个合数")
while a < end:
    if x % a == 0 and x != 2:
        print("%d是一个合数" % x)
        break
    else:
        a += 1
        if a < end:
            continue
        else:
            print("%d是一个素数" % x)