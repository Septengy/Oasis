"""
输入半径计算圆的周长和面积

Version: 0.1
题目作者: 骆昊
程序作者：Sep
"""

import math

r = float(input("半径 = "))
l = 2 * math.pi * r
s = math.pi * (r ** 2)
print("周长 = %.2f" % l)
print("面积 = %.2f" % s)
