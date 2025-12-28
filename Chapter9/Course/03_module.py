# 导模块（module）方式
"""
# 第一种：import 模块名
import time
print("开始")
time.sleep(1)
print("结束")


# 第二种：from 模块名 import 函数名
from time import sleep
print("开始")
sleep(1)
print("结束")


# 第三种：from 模块名 import *
# * 代表：把这个模块里面的所有东西都导进来
from time import *
print("开始")
sleep(1)
print("结束")


# 第四种：import 模块名 as 模块别名
import time as tt
tt.sleep(2)
print("hello")
"""

# 第五种：from 模块名 import 函数名 as 函数别名
from time import sleep as sl
sl(2)
print("hello")