# import my_package.my_module1
# from my_package.my_module1 import info_print
# from my_package.my_module2 import info_print

# my_package.my_module1.info_print1()
# info_print()

import my_package.my_module1
import my_package.my_module2

my_package.my_module1.info_print()
my_package.my_module2.info_print()