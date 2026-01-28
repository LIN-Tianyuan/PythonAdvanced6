# from pyecharts.charts import Map, Geo
# 导入pandas
import pandas as pd
from pyecharts.charts import Map, Page
from pyecharts.globals import ThemeType
from pyecharts.options import InitOpts, VisualMapOpts, LegendOpts, LabelOpts, TitleOpts, TextStyleOpts

# --------------- 数据清理 -----------------
dataset = pd.read_csv("owid-covid-data.csv")
# print(dataset.head())
# 把date这一列转换成datetime对象
dataset["date"] = pd.to_datetime(dataset["date"])
# 排序：按照日期倒序排列
df = dataset.sort_values(by=["date"], ascending=False)
# print(df.head())
# print(df.head()["date"])
# 取2022年8月1日的数据
map_df = df[df["date"] == "2022-08-01"]
# print(map_df)
# print(map_df["date"])
# 把索引index重置 从0开始
map_df.reset_index(drop=True, inplace=True)
# print(map_df)

country = list(map_df["location"])
# print(country)
total_cases = list(map_df["total_cases"])
# print(total_cases)

# 列表推导式 准备数据
final_list = [[country[i], total_cases[i]] for i in range(len(country))]
# print(final_list)

# 初始化地图对象
final_map = Map(InitOpts(width="1000px", height="460px", theme=ThemeType.ROMANTIC))
# 添加地图元素 把地图上位置点去掉
final_map.add("Total Confirmed Cases", final_list, maptype="world", is_map_symbol_show=False)
# 全局设置
final_map.set_global_opts(
    # 热力图的设置
    visualmap_opts=VisualMapOpts(max_=1100000, is_piecewise=True,
                                 pieces=[
                                     {"min": 500000},
                                     {"min": 200000, "max": 499999},
                                     {"min": 100000, "max": 199999},
                                     {"min": 50000, "max": 99999},
                                     {"min": 10000, "max": 49999},
                                     {"max": 9999}
                                 ]),
    # 图例的设置
    legend_opts=LegendOpts(is_show=False),
    # 标题的设置
    title_opts=TitleOpts(
        title="Covid-19 Worldwide Total Cases",
        subtitle="Till August 1st, 2022",
        pos_left="center",
        padding=0,
        item_gap=2,
        title_textstyle_opts=TextStyleOpts(
            color="darkblue",
            font_weight="bold",
            font_family="Courier New",
            font_size=30
        ),
        subtitle_textstyle_opts=TextStyleOpts(
            color="grey",
            font_weight="bold",
            font_family="Courier New",
            font_size=13
        ),
    )
)
# 局部设置
# 去除地图上的位置名
final_map.set_series_opts(label_opts=LabelOpts(is_show=False))

page = Page(layout=Page.SimplePageLayout)
page.add(final_map)
# 渲染地图
page.render()
