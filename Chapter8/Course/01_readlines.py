# 第一步：打开文件
f = open("python.txt", "r", encoding="utf-8")
# 第二步：读取文件
# readlines: 返回一个列表，包括所有文本，按每行去分隔
content = f.readlines()
print(content)
# 第三步：关闭文件
f.close()
