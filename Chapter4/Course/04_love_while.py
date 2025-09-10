# 外层循环 用来表示整个表白逻辑
i = 1
while i <= 100:
    print(f"Today is day {i}, Ready to confess my love.")
    # 内层循环 表白的具体步骤：送花 + 表白
    j = 1
    while j <= 10:
        print(f"Number of roses sent to Xiao Mei: {j}")
        j += 1
    print("Xiao Mei, I love you.")
    i += 1

print(f"Persistence to the number of days: {i-1}, show love successfully!")
