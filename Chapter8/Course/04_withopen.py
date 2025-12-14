# with的好处：代码少 不用手动关闭文件
with open("python.txt", "r") as f:
    print(f.readlines())