# -*- coding: utf-8 -*-
# @Time    : 2023/12/27 14:03
# @Author  : 居里夫人吃橘子
# @File    : test_process.py
# @Software: PyCharm

import unittest
from unittest import skip

from selenium import webdriver

from src.business.data.check_data_object_business import CheckDataObjectBusiness
from src.business.data.upload_data_business import UploadDataBusiness
from src.business.other.login_business import LoginBusiness


def skipTest(value):
    def deco(function):
        def wrapper(self, *args, **kwargs):
            if not getattr(self, value):
                self.skipTest('入库用例执行失败')
            else:
                function(self, *args, **kwargs)

        return wrapper

    return deco


# 流程测试
class ProcessTest(unittest.TestCase):
    driver = None
    upload_data_obj = None
    isOnline = False  # 未入库

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.upload_data_obj = UploadDataBusiness(self.driver)
        self.check_data_object_obj = CheckDataObjectBusiness(self.driver)
        self.upload_data_obj.open_url()
        LoginBusiness(self.driver).login_function('login_data.csv', 4)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    @skip
    def test_01_upload_vector_01(self):
        """矢量面文件上传"""
        self.upload_data_obj.open_url()

        try:
            # 文件上传业务
            self.upload_data_obj.uploaddata(2)
            actual_result = self.upload_data_obj.get_upload_text()
            self.assertEqual("导入成功1", actual_result)
            ProcessTest.isOnline = True  # 入库成功

        except Exception:
            self.upload_data_obj.get_screenshot("矢量文件上传")
            raise

    # @skipTest('isOnline')
    def test_02_check_geographical_info(self):
        """查看数据地理信息"""
        self.upload_data_obj.open_url()

        try:
            self.check_data_object_obj.input_first_object_overview('case1')
            actual_result = self.check_data_object_obj.get_geographical_position_text()
            print('数据地理位置为：{}'.format(actual_result))
            self.assertEqual("亚洲-中国", actual_result)

        except Exception:
            self.check_data_object_obj.get_screenshot('查看矢量地理坐标信息')
            raise

    # @skipTest('isOnline')
    def test_03_check_metadata_info(self):
        """查看元数据成果名称信息"""
        self.upload_data_obj.open_url()

        try:
            self.check_data_object_obj.check_metadata_info('case1')
            actual_result = self.check_data_object_obj.get_metadata_result_text()

            print('元数据成果名称：{}'.format(actual_result))
            self.assertEqual("region-GK", actual_result)

        except Exception:
            self.check_data_object_obj.get_screenshot('查看元数据成果名称信息')
            raise

    # @skipTest('isOnline')
    def test_04_check_content_info(self):
        """查看数据内容信息"""
        self.upload_data_obj.open_url()

        try:
            self.check_data_object_obj.check_data_content_info("case1")
            actual_result = self.check_data_object_obj.get_content_first_row_text()
            print('数据内容第一行第一列内容为：{}'.format(actual_result))
            self.assertEqual("2279", actual_result)

        except Exception:
            self.check_data_object_obj.get_screenshot('查看数据内容信息')
            raise


if __name__ == '__main__':
    unittest.TestCase()
