# 1. 打开文件
# "w"模式：write 会把之前的清空 然后重新写入内容
# 如果此时文件不存在，会自动创建一个新的文件
# 如果文件存在，会写到这个文件里
f = open("python.txt", "w", encoding="utf-8")
# 2. 写入文件
f.write("hello world2")
# 3. 刷新文件
f.flush()
# 4. 关闭文件
f.close()