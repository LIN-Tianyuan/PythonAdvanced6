# 定义一个列表
name_list = ['Leo', 'Lucas', 'Laurent']
print(name_list)
print(type(name_list))
print('----------')
# 列表里的元素可以是不同类型的
my_list = ['Alex', 666, True]
print(my_list)
print(type(my_list))
print('----------')
my_list2 = [1, 2, 3, 4, 5, 6]
my_list3 = [[1, 2, 3], [4, 5, 6]]
# 获取列表的长度
print(len(my_list2))    # 6
print(len(my_list3))    # 2
# 获取嵌套列表里的元素
print(my_list3[0][1])   # 2
print(my_list3[1][2])   # 6
print('----------')
name_list2 = ['Leo', 'Lucas', 'Laurent']
# 通过index取出相应的元素（index是从0开始的）
print(name_list2[1])
print(name_list2[-1])


