# -*- coding: utf-8 -*-
# @Time : 2022/10/12 16:21
# @Author : 居里夫人吃橘子
# @Site : 
# @File : app_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class AppPage(BasePage):
    # 数据导入按钮
    data_import_btn_ele = (By.XPATH,'//p[text()="数据导入"]/../../div[@class="textdata-imger"]')

    # 点击数据导入
    def click_data_import_btn(self):
        self.find_element_explicitly(self.data_import_btn_ele).click()
