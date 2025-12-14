def test_func(compute):
    result = compute(1, 2)
    print(result)

# 用def定义一个有名字的函数
def compute(x, y):
    return x + y

# 传入定义好的函数compute
test_func(compute)

# 用lambda定义一个匿名函数（临时函数）
# lambda 传入参数：函数体（一行代码）
test_func(lambda x, y: x + y)