from random import randint

def roll_dice(n = 2):
    """
    摇骰子
    :param n: 骰子数量默认为2，可手动输入其他正整数
    :return: total所有骰子的点数和
    """
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


# 若没有指定参数，则使用默认数值摇骰子
print(roll_dice())
# 摇三颗骰子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递函数可以不按照设定顺序进行传递
print(add(c=100, a=20, b=10))
