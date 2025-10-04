num = 100

def test_a():
    print(num)

def test_b():
    # num = 200
    # print(num)
    # global的作用：就是让里面不要创建新的局部变量num，使用全局变量num
    global num
    num = 200
    print(num)

test_a()
test_b()
print(f"全局变量的num值为：{num}")