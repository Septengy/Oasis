"""
输入年份 如果是闰年输出True 否则输出False

Version: 0.1
题目作者: 骆昊
程序作者: Sep
"""
year = int(input("请输入年份："))
var = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(var)