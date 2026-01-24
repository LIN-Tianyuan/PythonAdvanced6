import json
from pyecharts.charts import Line

# 打开文件
with open("America.txt") as f:
    # 读取文件数据 readlines是获取到一个数据列表
    data_list = f.readlines()
    # 获取列表数据 去掉列表带的中括号
    us_data = data_list[0]
    # 去掉无用的字符串 用切片slice
    us_data = us_data[us_data.index("(") + 1:len(us_data) - 2]
    # 把json转换成Python的字典dict
    us_dict = json.loads(us_data)
    # 拿到trend data
    trend_data = us_dict["data"][0]["trend"]
    # print(trend_data)
    # 拿到更新的日期updateDate作为x轴
    x_data = trend_data["updateDate"][:314]
    # 拿到确诊人数的数据作为y轴
    y_data = trend_data["list"][0]["data"]

# 获取线性图表Line对象
line = Line()
line.add_xaxis(x_data)
line.add_yaxis("America", y_data)
line.render()
