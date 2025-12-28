"""
try:
    # 可能发生错误的代码
    f = open("linux.txt", "r")
except:
    # 如果有错误，执行这里的代码
    # 必须是创建文件
    f = open("linux.txt", "w")

name = "alex"
try:
    print(name)
except NameError as e:
    print("变量未定义")

try:
    print(1 / 0)
except (ZeroDivisionError, NameError):
    print("Erreur de ZéroDivision ...")

try:
    print(age)
except NameError as e:
    print(e)
"""

"""
try:
    print(name)
except Exception as e:
    print(e)
# else: 里面的代码是当没有异常的时候会走到这
else:
    print("我是else，当没有异常的时候会运行到这里")
"""

try:
    f = open("test.txt", "r")
except Exception as e:
    f = open("test.txt", "w")
else:
    print("没有异常，正常运行")
# 无论是否有异常，都会走这里
finally:
    f.close()

