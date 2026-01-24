import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts, InitOpts, LineStyleOpts

line = Line(InitOpts(width="1200px", height="600px"))
line.add_xaxis(["France", "America", "China"])
line.add_yaxis("GDP", [30, 20, 10], symbol_size=10, label_opts=LabelOpts(), linestyle_opts=LineStyleOpts(width=2))
line.render()