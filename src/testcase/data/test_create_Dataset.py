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
        LoginBusiness(cls.driver).login_judge('1')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_create_set_01(self):
        """新建矢量数据集"""
        try:
            self.create_datatask_obj.create_set(2)
            actual_result = self.create_datatask_obj.get_info_createset_prompt()
            self.create_datatask_obj.refresh_driver()
            self.assertEqual('新建数据集成功', actual_result)

        except:
            self.create_datatask_obj.get_screenshot('创建矢量数据集')
            raise

    def test_create_set_02(self):
        """新建正射数据集"""
        try:
            self.create_datatask_obj.create_set(3)
            actual_result = self.create_datatask_obj.get_info_createset_prompt()
            self.create_datatask_obj.refresh_driver()
            self.assertEqual('新建数据集成功', actual_result)

        except:
            self.create_datatask_obj.get_screenshot('创建正射数据集')
            raise
