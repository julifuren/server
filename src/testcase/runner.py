# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 17:34
# @Author  : 居里夫人吃橘子
# @File    : runner.py
# @Software: PyCharm
import os
from src.common.common_operation import common_operate_obj
import unittest
from BeautifulReport import BeautifulReport

# 用例存放位置
test_case_path = r"D:\PythonTest\PIE_Server\src\testcase\data"

# 测试报告存放位置
log_path = r'D:\PythonTest\PIE_Server\reports'

# 测试报告名称
filename = f"report_{common_operate_obj.time_stamp()}"

# 用例名称
description = 'server自动化测试用例'

# 需要执行哪些用例，如果目录下的全部，可以改为"*.py"，如果是部分带test后缀的，可以改为"*test.py"
pattern = "test_upload_data.py"

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover(test_case_path, pattern=pattern)
    result = BeautifulReport(test_suite)
    result.report(filename=filename, description=description, log_path=log_path)
