# -*- coding: utf-8 -*-
# @Time : 2022/3/18 15:06
# @Author : 居里夫人吃橘子
# @Site : 
# @File : parse_csv.py
# @Software: PyCharm


import os, csv

from src.common import common_operation
# 定义一个类，用来实现读取csv文件中的测试数据和配置数据。
class ParseCsv():
    # 1、首先要找到要读取的csv这个文件，使用os模块
    #  为了让实例化的对象有意义，所有建议 把 文件的路径放在 构造方法中。以参数形式来接收CSV文件的路径。
    def __init__(self, parent_path, file_name):
        """
        :param parent_path:  表示要读取的csv文件所在的目录。
        :param file_name:    表示要读取的csv文件的名称。
        """
        self.parent_path = parent_path    # 重新进行赋值，是因为在  read_value_of_csv 这个方法中需要 用到它 做判断。
        # project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 这行代码使用 函数替换掉了
        self.csv_path = os.path.join(common_operation.common_operate_obj.get_project_path(), parent_path, file_name)

    # 因为读取 测试数据文件 和 读取配置数据文件的代码基本是一样的，代码存在冗余，所以可以进行优化。
    def read_value_of_csv(self, row_num=None):
        if self.parent_path in ["data", "config"]:
            # 2、打开csv文件（使用open函数）
            with open(self.csv_path, encoding="GB2312") as csvfile:
                # 3、读取csv 文件中的内容  （使用到 python自带的一个模块：csv）
                # 使用csv.reader()方法返回的是一个 csv 阅读器（本质是 迭代器）。
                reader = csv.reader(csvfile)
                # print(type(reader))
                # 需要进行判断，判断要读取的是 测试数据 还是 配置数据，如果读取的是 测试数据 则转换成 列表，如果读取是 配置数据在，则转换成字典。
                if self.parent_path == "data":
                    data_list = list(reader)
                    return data_list[row_num - 1]
                elif self.parent_path == "config":
                    data_dict = dict(reader)
                    # 5、返回整个字典，因为所有的内容都需要用到。
                    return data_dict
        # 如果输入的目录不存在， 则抛出异常！
        else:
            raise Exception("文件或者路径不存在，请确认！！！")

if __name__ == '__main__':
    test = ParseCsv('data', 'biaoshi.csv').read_value_of_csv(2)
    print(test)
    print(type(test))