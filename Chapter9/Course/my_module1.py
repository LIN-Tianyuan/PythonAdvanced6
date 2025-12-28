def test(a, b):
    print(a + b)

# 只在运行此文件时，会调用，导模块时不会调用
if __name__ == "__main__":
    test(1, 1)