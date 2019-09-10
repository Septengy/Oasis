"""
掷骰子决定做什么事情

Version: 0.1
题目作者: 骆昊
程序作者: Sep
"""

from random import randint

face = randint(1, 6)
if face == 1:
    print("去吃麦当劳")
elif face == 2:
    print("去吃食堂")
elif face == 3:
    print("去吃老碗面")
elif face == 4:
    print("去吃米粟米")
elif face == 5:
    print("去吃赛百味")
elif face == 6:
    print("你可别吃了！")