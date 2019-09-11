"""
寻找水仙花数
水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、
自恋数、自幂数、阿姆斯壮数或阿姆斯特朗数（Armstrong number），水仙花数是指一个 3 位数，它的每个位上的
数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。
"""
for z in range(1, 10, 1):
    for y in range(10):
        for x in range(10):
            a = 100 * z + 10 * y + x
            if a == z ** 3 + y ** 3 + x ** 3:
                print(a)