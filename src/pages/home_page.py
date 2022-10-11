# -*- coding: utf-8 -*-
# @Time : 2022/4/18 15:04
# @Author : 居里夫人吃橘子
# @Site : 
# @File : home_page.py
# @Software: PyCharm
from time import sleep

from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage

# 首页 页面元素和操作
class HomePage(BasePage):

    # 应用 按钮
    app_btn_ele = (By.XPATH,'//div[@class="nav-list"]//span[text()="应用"]')

    def click_app_btn(self):
        sleep(2)
        self.find_element_explicitly(self.app_btn_ele).click()


