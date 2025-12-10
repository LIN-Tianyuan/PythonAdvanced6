my_list = [1, 2, 3]
my_tuple = (1, 2, 3, 4, 5)
my_str = "Python"

# 获取容器的长度（元素个数）
print(len(my_list))
print(len(my_tuple))
print(len(my_str))
print("----------")
# 求容器的最大元素
print(max(my_list))
print(max(my_tuple))
print(max(my_str))
print("----------")
# 求容器的最小元素
print(min(my_list))
print(min(my_tuple))
print(min(my_str))
print("----------")
my_list2 = [1, 2, 3, 3, 4, 4, 5]
# set(容器) 可以用于去重
my_set2 = set(my_list2)
new_list2 = list(my_set2)
print(new_list2)
print("----------")
my_list3 = [5, 2, 3, 3, 4, 4, 5, 6, 1]
# 对列表进行排序（默认是升序排列）
print(sorted(my_list3))
# 列表元素降序排列（reverse=True）
print(sorted(my_list3, reverse=True))
print("----------")
# Bubble sort 冒泡排序
my_list3 = [5, 2, 3, 3, 4, 4, 5, 6, 1]
i = 0
n = len(my_list3) # 9
while i < n:
    j = 0
    while j < n - i - 1:
        if my_list3[j] > my_list3[j + 1]:
            temp = my_list3[j]
            my_list3[j] = my_list3[j + 1]
            my_list3[j + 1] = temp
        j = j + 1
    i = i + 1

print(my_list3)
print("----------")

print("abc" > "abd")
print("a" > "A")
print("key2" > "key1")
print("by" > "ca")




