# 字符串str的特点：是一个不可被改变的容器
name = "Alex"
print(name[0])
print(name[-1])
print(name.index("e"))
print("----------")
name_string1 = "Leo and laurent"
print(name_string1.index("and"))
print("----------")
name_string2 = "Leo and laurent"
name_string3 = name_string2.replace("Leo", "Kevin")
print(name_string2)
print(name_string3)
print("----------")
name_string4 = "Leo and laurent"
# 以空格作为分隔符 获取子字符串列表
name_list = name_string4.split(" ")
print(name_list)
print("----------")
name_string5 = "  Leo and laurent  "
# 去掉字符串前后的空格
name_string6 = name_string5.strip()
print(name_string6)
name_string7 = name_string5.replace(" ", "")
print(name_string7)
print("----------")
name_string8 = "12Leo and laurent21"
# 去掉字符串前后指定的元素
name_string9 = name_string8.strip("12")
print(name_string9)
print("----------")
name_string10 = "Jean-Lucas and Lucas"
# 得到指定子字符串的出现次数
print(name_string10.count("Lucas"))
# 获取字符的个数  char(character) string
print(len(name_string10))