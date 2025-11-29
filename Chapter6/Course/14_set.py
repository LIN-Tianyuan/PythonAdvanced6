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
print("-----------")
set1 = {1, 2, 3}
set2 = {1, 5, 6}
# 拿set1里的元素，但是又不在set2里的
set3 = set1.difference(set2)
print(set3)
print(set1)
print(set2)
print("-----------")
set3 = {1, 2, 3}
set4 = {1, 5, 6}
# 删除掉set4里的所有set3里也存在的元素
set3.difference_update(set4)
print(set3)
print(set4)
print("-----------")
set5 = {1, 2, 3}
set6 = {1, 5, 6}
# 将两个set的元素融合到一个新set
set7 = set5.union(set6)
print(set7)
print(set5)
print(set6)
# 获取set的长度
print(len(set5))
print("-----------")
# set的遍历
set8 = {1, 2, 3}
for i in set8:
    print(i)

