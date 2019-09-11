"""
输入两个正整数计算最大公约数和最小公倍数

Version: 0.1
题目作者: 骆昊
程序作者: Sep
出题时间: 2018-03-01
编写时间: 2019-09-11
"""
a = int(input("请输入正整数a："))
b = int(input("请输入正整数b："))
if a > b:
    a, b = b, a
for factor in range (a, 0, -1):
    if a % factor == 0 and b % factor ==0:
        print('%d和%d的最大公约数是%d' % (a, b, factor))
        print('%d和%d的最小公倍数是%d' % (a, b, a * b // factor))
        break