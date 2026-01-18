# 导入json模块
import json

# Python数据：list
data = [{"name": "Kevin", "age": 16}, {"name": "Laurent", "age": 20}]
print(len(data))
print(type(data))
print(type(data[0]))

# 把Python格式的数据转换为json
# json本质其实就是一个固定格式（大家规定好的）的字符串
data = json.dumps(data)
print(data)
print(type(data))

# 把json格式的数据转换成python的数据类型
data = json.loads(data)
print(data)
print(type(data))

