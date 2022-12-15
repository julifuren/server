# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 17:34
# @Author  : 居里夫人吃橘子
# @File    : runner.py
# @Software: PyCharm
import os
import unittest

from BeautifulReport import BeautifulReport
from src.common.common_operation import common_operate_obj

#获取测试用例路径
testcase_path = os.path.join(common_operate_obj.get_project_path(), "src", "testcase")

# 获取到测试套件
suite = unittest.defaultTestLoader.discover(testcase_path)

# 获取到 测试报告 存放的目录
report_path = os.path.join(common_operate_obj.get_project_path(), "reports")

# 执行测试用例，并生成测试报告。
BeautifulReport(suite).report(description="server数据导入自动化测试报告", filename=f"report_{common_operate_obj.time_stamp()}", log_path=report_path)




