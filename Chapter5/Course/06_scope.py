"""
def test_a():
    # 局部变量 local variable : 只有函数内部可以使用
    num = 100
    print(num)

test_a()
# 当调用函数结束后，函数里面的局部变量会被销毁
# test_a()
print(num)
"""

# 全局变量 global variable : 函数内外都可以使用
num = 100
def test_a():
    print(num)

def test_b():
    print(num)

test_a()
test_b()
print(num)

