"""
输出乘法口诀表(九九表)

Version: 0.1
题目作者: 骆昊
拷贝: Sep
"""

for a in range(1, 10):
    for b in range(1, a+1):
        print("%d * %d = %d" % (a, b, a * b), end='\t')
    print()
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
"""