# __all__: 当使用from xxx import * 的时候，只有这里面的函数（元素）可以被导入
__all__ = ["test_a"]

def test_a():
    print("test A")

def test_b():
    print("test B")