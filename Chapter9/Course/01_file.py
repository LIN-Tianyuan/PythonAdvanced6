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

