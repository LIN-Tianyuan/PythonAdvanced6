my_list = [1, 2, 3, 4, 5]
new_list = my_list[1:4]     # 取头不取尾
print(new_list)
print("----------")
my_tuple = (1, 2, 3, 4, 5)
my_tuple1 = my_tuple[:4]
print(my_tuple1)
my_tuple2 = my_tuple[1:]
print(my_tuple2)
my_tuple3 = my_tuple[:]
print(my_tuple3)
print("----------")
my_list1 = [1, 2, 3, 4, 5]
# begin:end:step
new_list1 = my_list1[::2]
print(new_list1)
new_list2 = my_list1[1::2]
print(new_list2)
print("----------")
my_str = "12345"
new_str = my_str[:4:2]
print(new_str)
print("----------")
my_str1 = "12345"
new_str1 = my_str1[::-1]
print(new_str1)
print("----------")
my_list2 = [1, 2, 3, 4, 5]
new_list3 = my_list2[3:1:-1]
print(new_list3)
print("----------")
my_tuple4 = (1, 2, 3, 4, 5)
new_tuple4 = my_tuple4[:1:-2]
print(new_tuple4)

