# 在参数名前面的*表示args是一个可变参数
# 即在调用add函数时可以传入0个或多个参数
def add(*var):
    total = 0
    for a in var:
        total += a
    return  total

print(add(1, 2, 4))