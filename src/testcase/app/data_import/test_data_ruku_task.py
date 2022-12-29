# -*- coding: utf-8 -*-
# @Time : 2022/10/18 17:04
# @Author : 居里夫人吃橘子
# @Site : 
# @File : test_data_ruku_task.py
# @Software: PyCharm
import unittest

from selenium import webdriver

from src.business.app.data_import.create_datatask_business import CreateDatataskBusiness
from src.business.other.login_business import LoginBusiness


class CreateDataTaskBusinessCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

        self.create_datatask_obj = CreateDatataskBusiness(self.driver)

        self.create_datatask_obj.open_url()

        LoginBusiness(self.driver).login_add_cookies()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_cdt_verctor_84_01(self):
        """矢量数据2000坐标系入库测试"""
        try:
            self.create_datatask_obj.create_datatask(2)
            #获取
            status = self.create_datatask_obj.assert_taskname_text()
            self.assertEqual('完成', status)

        except:
            self.create_datatask_obj.get_screenshot('矢量2000入库测试')
            raise

    def test_cdt_verctor_84_02(self):
        """矢量数据84坐标系入库测试"""
        try:
            self.create_datatask_obj.create_datatask(3)
            # 获取
            status = self.create_datatask_obj.assert_taskname_text()
            self.assertEqual('完成', status)

        except:
            self.create_datatask_obj.get_screenshot('矢量84入库测试')
            raise

    def test_cdt_dom_UTM_01(self):
        """正射数据UTM投影入库测试"""
        try:
            self.create_datatask_obj.create_datatask(4)
            # 获取
            status = self.create_datatask_obj.assert_taskname_text()
            self.assertEqual('完成', status)

        except:
            self.create_datatask_obj.get_screenshot('正射数据UTM投影')
            raise
