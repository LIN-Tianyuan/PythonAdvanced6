name_list = ['Leo', 'Lucas', 'Laurent']
# 找出元素的下标 index
print(name_list.index('Lucas'))
# 修改列表的元素
name_list[1] = 'Alex'
print(name_list)
# 添加元素到列表的任意位置（通过下标）
name_list.insert(1, 'Kevin')
print(name_list)
# 添加元素到列表末尾
name_list.append('Luna')
print(name_list)
print('----------')
my_list = [1, 2, 3]
# 修改列表的元素
my_list[0] = 5
print(my_list)
my_list2 = [1, 2, 3]
# 添加元素到列表末尾
my_list2.append(4)
print(my_list2)     # [1, 2, 3, 4]
my_list3 = [1, 2, 3]
my_list3.append([4, 5, 6])
print(my_list3)     # [1, 2, 3, [4, 5, 6]]
my_list4 = [1, 2, 3]
# 把其他容器的值拿出来后再添加到列表
my_list4.extend([4, 5, 6])
print(my_list4)     # [1, 2, 3, 4, 5, 6]
my_list5 = [1, 2, 3]
# 第一种删除：del   (非常少用）
del my_list5[2]
print(my_list5)     # [1, 2]
my_list6 = [1, 2, 3]
# 第二种删除：pop   通过下标去删除对应元素
print(my_list6.pop(2))
print(my_list6)     # [1, 2]
my_list7 = [1, 2, 3]
# 第三种删除：remove   通过元素直接删除
my_list7.remove(3)
print(my_list7)     # [1, 2]
my_list8 = [1, 2, 3, 2, 3]
# 如果有多个相同元素在列表里，remove只删除第一个元素
my_list8.remove(2)
print(my_list8)
my_list9 = [1, 2, 3]
# 清空列表
my_list9.clear()
print(my_list9)
my_list9 = [1, 1, 1, 2, 3]
# 计算某个元素出现的次数
print(my_list9.count(1))


