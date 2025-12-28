def func01():
    print("函数01的开始")
    num = 1 / 0
    print("函数01的结束")

def func02():
    print("函数02的开始")
    func01()
    print("函数02的结束")

def main():
    try:
        func02()
    except Exception as e:
        print(e)

# 异常是有传递性的
main()
