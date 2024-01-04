# -*- coding: utf-8 -*-
# @Time    : 2023/3/16 20:13
# @Author  : 居里夫人吃橘子
# @File    : test_create_Dataset.py
# @Software: PyCharm
import unittest
from selenium import webdriver

from src.business.data.create_data_set_business import CreateDataSetBusiness
from src.business.other.login_business import LoginBusiness


class CreateDataSetCase(unittest.TestCase):
    create_datatask_obj = None
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.create_datatask_obj = CreateDataSetBusiness(cls.driver)
        cls.create_datatask_obj.open_url()
        LoginBusiness(cls.driver).login_function('login_data.csv', 4)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_create_set_01(self):
        """新建矢量数据集"""
        self.create_datatask_obj.open_url()
        try:
            self.create_datatask_obj.create_set('case1')
            actual_result = self.create_datatask_obj.get_info_createset_prompt()
            self.assertEqual(actual_result, '新建数据集成功')

        except:
            self.create_datatask_obj.get_screenshot('新建矢量数据集')
            raise

    def test_create_set_02(self):
        """新建影像数据集"""
        self.create_datatask_obj.open_url()
        try:
            self.create_datatask_obj.create_set('case2')
            actual_result = self.create_datatask_obj.get_info_createset_prompt()
            self.assertEqual(actual_result, '新建数据集成功')

        except:
            self.create_datatask_obj.get_screenshot('新建影像数据集')
            raise

    def test_create_set_03(self):
        """新建json数据集"""
        self.create_datatask_obj.open_url()
        try:
            self.create_datatask_obj.create_set('case3')
            actual_result = self.create_datatask_obj.get_info_createset_prompt()
            self.assertEqual(actual_result, '新建数据集成功')

        except:
            self.create_datatask_obj.get_screenshot('新建json数据集')
            raise

    def test_create_set_04(self):
        """新建地理数据库数据集"""
        self.create_datatask_obj.open_url()
        try:
            self.create_datatask_obj.create_set('case4')
            actual_result = self.create_datatask_obj.get_info_createset_prompt()
            self.assertEqual(actual_result, '新建数据集成功')

        except:
            self.create_datatask_obj.get_screenshot('新建地理数据库数据集')
            raise

    def test_create_set_05(self):
        """新建坐标文件数据集"""
        self.create_datatask_obj.open_url()
        try:
            self.create_datatask_obj.create_set('case5')
            actual_result = self.create_datatask_obj.get_info_createset_prompt()
            self.assertEqual(actual_result, '新建数据集成功')

        except:
            self.create_datatask_obj.get_screenshot('新建坐标文件数据集')
            raise

    def test_create_set_06(self):
        """新建文档文件数据集"""
        self.create_datatask_obj.open_url()
        try:
            self.create_datatask_obj.create_set('case6')
            actual_result = self.create_datatask_obj.get_info_createset_prompt()
            self.assertEqual(actual_result, '新建数据集成功')

        except:
            self.create_datatask_obj.get_screenshot('新建文档文件数据集')
            raise

    def test_create_set_07(self):
        """新建多媒体数据集"""
        self.create_datatask_obj.open_url()
        try:
            self.create_datatask_obj.create_set('case7')
            actual_result = self.create_datatask_obj.get_info_createset_prompt()
            self.assertEqual(actual_result, '新建数据集成功')

        except:
            self.create_datatask_obj.get_screenshot('新建多媒体数据集')
            raise

    def test_create_set_08(self):
        """新建DEM数据集"""
        self.create_datatask_obj.open_url()
        try:
            self.create_datatask_obj.create_set('case8')
            actual_result = self.create_datatask_obj.get_info_createset_prompt()
            self.assertEqual(actual_result, '新建数据集成功')

        except:
            self.create_datatask_obj.get_screenshot('新建DEM数据集')
            raise

    def test_create_set_09(self):
        """新建倾斜摄影数据集"""
        self.create_datatask_obj.open_url()
        try:
            self.create_datatask_obj.create_set('case9')
            actual_result = self.create_datatask_obj.get_info_createset_prompt()
            self.assertEqual(actual_result, '新建数据集成功')

        except:
            self.create_datatask_obj.get_screenshot('新建倾斜摄影数据集')
            raise


if __name__ == '__main__':
    unittest.TestCase()
