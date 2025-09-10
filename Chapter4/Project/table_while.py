# 外层循环 控制行数
j = 1
while j <= 9:
    # 内层循环 控制列数
    i = 1
    while i <= j:
        print(f"{i} * {j} = {i*j}", end="\t")
        i += 1
    print()
    j += 1

