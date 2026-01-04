# __init__.py：这个文件就是表明，它所在的文件夹是一个Python Package
# 一个Python Package就是 装了__init__.py 还有其他的module(python 文件)
# __all__：去控制哪些模块module可以被导入 适用于导包或者导模块的时候用了*号的场景
# 三层：package -> module -> function(method, variable, class)
__all__ = ["my_module1", "my_module2"]

