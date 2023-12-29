# -*- coding: utf-8 -*-
# @Time    : 2023/11/2 16:15
# @Author  : 居里夫人吃橘子
# @File    : test_upload_data.py
# @Software: PyCharm
import unittest
from unittest import skip

from selenium import webdriver

from src.business.data.upload_data_business import UploadDataBusiness
from src.business.other.login_business import LoginBusiness


class UploadData(unittest.TestCase):
    driver = None
    upload_data_obj = None

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.upload_data_obj = UploadDataBusiness(self.driver)
        self.upload_data_obj.open_url()
        LoginBusiness(self.driver).login_function('login_data.csv', 4)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_upload_vector_01(self):
        """矢量面文件上传"""
        self.upload_data_obj.open_url()
        try:
            # 文件上传业务
            self.upload_data_obj.uploaddata(2)
            actual_result = self.upload_data_obj.get_upload_text()
            self.assertEqual("导入成功", actual_result)

        except:
            self.upload_data_obj.get_screenshot("矢量文件上传")
            raise

    @skip
    def test_upload_json_01(self):
        """矢量json文件上传"""
        self.upload_data_obj.open_url()
        try:
            # 文件上传业务
            self.upload_data_obj.uploaddata(5)

            actual_result = self.upload_data_obj.get_upload_text()
            self.assertEqual("导入成功", actual_result)

        except:
            self.upload_data_obj.get_screenshot("矢量json文件上传")
            raise

    @skip
    # 用例2：15兆影像文件上传
    def test_upload_dom_01(self):
        """影像文件上传"""
        self.upload_data_obj.open_url()
        try:
            # 文件上传业务
            self.upload_data_obj.uploaddata(3)

            actual_result = self.upload_data_obj.get_upload_text()
            self.assertEqual("导入成功", actual_result)

        except:
            self.upload_data_obj.get_screenshot("影像文件上传")
            raise

    @skip('300m跳过')
    def test_upload_dom_02(self):
        """影像300m文件上传"""
        self.upload_data_obj.open_url()
        try:
            # 文件上传业务
            self.upload_data_obj.uploaddata(4, 160)
            actual_result = self.upload_data_obj.get_upload_text(120)
            self.assertEqual("导入成功", actual_result)

        except:
            self.upload_data_obj.get_screenshot("影像300m文件上传")
            raise


if __name__ == '__main__':
    unittest.TestCase()
