"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积

Version: 0.1
题目作者: 骆昊
程序作者: Sep
"""
import math

a = float(input("请输入线段a的长度："))
b = float(input("请输入线段b的长度："))
c = float(input("请输入线段c的长度："))
if (a + b) > c and (a + c) > b and (b + c) > a:
    l = a + b + c
    print("三角形周长 = %.2f" % (a + b + c))
    s = (a + b + c)/2
    A = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("三角形面积 = %.2f" % A)
else:
    print("这三条线段无法构成三角形")