# 定义字典 dict      key:value
stu_score = {"Luna": 99, "Alex": 88, "Laurent": 77}
# 获取字典的长度
print(len(stu_score))
# 类型：dict
print(type(stu_score))
# 查字典 获取字典的指定value
print(stu_score["Luna"])
print("----------")
stu_score2 = {
    "Luna": {
        "English": 33,
        "Chinese": 77,
        "Math": 66
    },
    "Alex": {
        "English": 55,
        "Chinese": 88,
        "Math": 86
    },
    "Laurent": {
        "English": 66,
        "Chinese": 99,
        "Math": 96
    }
}
print(stu_score2["Alex"]["Math"])
print(stu_score2["Luna"])
print("----------")
stu_score3 = {"Luna": 99, "Alex": 88, "Laurent": 77}
# 字典添加元素
stu_score3["Tom"] = 66
print(stu_score3)
print("----------")
stu_score4 = {"Luna": 99, "Alex": 88, "Laurent": 77}
# 修改字典元素
stu_score4["Laurent"] = 55
print(stu_score4)
print("----------")
stu_score5 = {"Luna": 99, "Alex": 88, "Laurent": 77}
# 通过key删除元素
score = stu_score5.pop("Laurent")
print(score)
print(stu_score5)
print("----------")
# 清除所有元素
stu_score5.clear()
print(stu_score5)
stu_score6 = {"Luna": 99, "Alex": 88, "Laurent": 77}
print("----------")
# 第一种遍历
for i in stu_score6:
    print(f"key: {i} value: {stu_score6[i]}")
print("----------")
# 第二种遍历
keys = stu_score6.keys()
for key in keys:
    print(f"Student: {key} Score: {stu_score6[key]}")

