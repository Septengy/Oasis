"""
用for循环实现1~100之间的偶数求和

Version: 0.1
题目作者: 骆昊
拷贝: Sep
"""
sum = 0
for x in range(101):
    if x % 2 == 0:
        sum += x
print(sum)