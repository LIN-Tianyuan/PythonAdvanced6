"""
import my_module1

# 计算2加3
my_module1.test(2, 3)


from my_module1 import test
# 计算2加3
test(2, 3)


from my_module1 import test
from my_module2 import test

test(2, 3)


import my_module1
import my_module2

my_module1.test(2, 3)
my_module2.test(2, 3)
"""

from my_module3 import *
test_a()
test_b()


