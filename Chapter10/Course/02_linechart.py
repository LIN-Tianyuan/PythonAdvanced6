# 导入pyecharts模块
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 1. 获取线性图表Line对象
line = Line()
# 2. 添加x轴
line.add_xaxis(["France", "America", "China"])
# 3. 添加y轴
line.add_yaxis("GDP", [30, 20, 10])
line.set_global_opts(
    # 标题的具体设置
    title_opts=TitleOpts(title="GDP Show", pos_left="center", pos_bottom="1%"),
    # 图例的具体设置
    legend_opts=LegendOpts(is_show=True),
    # 工具箱的具体设置
    toolbox_opts=ToolboxOpts(),
    # 热力图的具体设置
    visualmap_opts=VisualMapOpts()
)
# 4. 渲染图表
line.render()
