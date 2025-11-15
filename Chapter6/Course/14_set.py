# 定义一个集合 set
name = {"Python", "666", "Python", "y6"}
print(name)

# set的两大特点：去重 无序
print("-----------")
my_set = {"Leo", "Laurent"}
# 添加一个元素
my_set.add("Kevin")
print(my_set)
print("-----------")
my_set1 = {"Leo", "Laurent", "Kevin"}
# 随机删除元素
name = my_set1.pop()
print(name)
print(my_set1)
print("-----------")
my_set2 = {"Leo", "Laurent", "Kevin"}
# 删除指定元素
my_set2.remove("Leo")
print(my_set2)
print("-----------")
# 清除所有元素
my_set2.clear()
print(my_set2)

