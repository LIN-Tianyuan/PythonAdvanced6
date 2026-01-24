from pyecharts.charts import Map, Geo
import pandas as pd

dataset = pd.read_csv("owid-covid-data.csv")
print(dataset.head())