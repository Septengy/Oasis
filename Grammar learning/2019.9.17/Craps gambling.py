"""
craps赌博游戏

规则：玩家掷两个骰子，每个骰子点数为1-6，如果第一次点数和
为7或11，则玩家胜；如果点数和为2、3或12，则玩家输庄家胜。
若和为其他点数，则记录第一次的点数和，玩家继续掷骰子，直至
点数和等于第一次掷出的点数和则玩家胜；若掷出的点数和为7则庄
家胜。

程序作者: Sep
"""
import random
import sys

a = random.randint(1, 6)
b = random.randint(1, 6)
print(a, b)
c = a + b
if c == 7 or c == 11:
    print("你赢了！")
    sys.exit()
if c == 2 or c == 3 or c == 12:
    print("你输了")
    sys.exit()
while True:
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    print(a, b)
    if a + b == c:
        print("你赢了！")
        break
    if a + b == 7:
        print("你输了")
        break