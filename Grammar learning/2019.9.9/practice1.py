"""
英制单位英寸和公制单位厘米互换

Version: 0.1
题目作者: 骆昊
程序作者: Sep
"""
s = float(input("请输入长度："))
unit = input("请输入单位（英寸/厘米）：")
if unit == "英寸":
    y = s * 2.54
    print("%.2f英寸 = %.2f厘米" % (s, y))
else:
    y = s / 2.54
    print("%.2f厘米 = %.2f英寸" % (s, y))
