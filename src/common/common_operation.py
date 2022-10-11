# -*- coding: utf-8 -*-
# @Time : 2022/3/18 15:07
# @Author : 居里夫人吃橘子
# @Site : 
# @File : common_operation.py
# @Software: PyCharm
import os
import time
import warnings
# 这里只能导入的是模块。不能直接导入 该模块（parse_csv.py）中的类。
from src.common import parse_csv

# 定义一个类，用来实现 通用的操作。 获取 工程所在的目录、获取系统当前时间的功能
class CommonOperate():
    # 定义一个方法，用来实现获取工程目录的功能
    def get_project_path(self):
        return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # 定义一个方法，用来实现获取系统当前的时间。 年月日时分秒   24 小时制
    def time_stamp(self):
        return time.strftime("%Y%m%d_%H-%M-%S")

# 为了避免多次实例化占用内存空间，可以提前实例化一个对象出来。只需要在这里实例化一次即可。
common_operate_obj = CommonOperate()

if __name__ == '__main__':
    print(CommonOperate().get_project_path())
    print(CommonOperate().time_stamp())
    # sql = 'SELECT password FROM stfoa.`oa_tbl_employee` WHERE loginid = "fuc";'
    # print(common_operate_obj.execute_sql(sql)[0][0])

