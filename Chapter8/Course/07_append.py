# 1. 打开文件
# "a"模式：append 追加内容到后面
# 如果此时文件不存在，会自动创建一个新的文件
# 如果文件存在，会追加到这个文件的内容后面
f = open("python.txt", "a")
# 2. 写入文件
f.write("\nhello world")
# 3. 刷新文件
f.flush()
# 4. 关闭文件
f.close()