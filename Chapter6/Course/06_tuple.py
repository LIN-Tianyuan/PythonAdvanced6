# 定义元组
t1 = (1, 2, "hello")
print(t1)
print(type(t1))

# 查看元组的元素个数
print(len(t1))
# 查看元素的下标index
print(t1.index(2))
# 获取对应下标的元素
print(t1[2])
print("----------")
t2 = (1, 2, "hello", 3, 4, "hello")
# 返回下标时默认找第一个元素
print(t2.index("hello"))
# 计算元组里有多少个指定元素
print(t2.count("hello"))
print("----------")
t3 = (1, 2, ["Leo", "Laurent"])
t3[2][0] = "Alex"
print(t3)
