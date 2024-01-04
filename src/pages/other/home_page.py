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
    app_btn_ele = (By.XPATH, '//div[@class="nav-list"]//span[text()="应用"]')
    # 数据 按钮
    data_btn_ele = (By.XPATH, '//span[@class="item-text" and text()="数据"]')
    # 集市 按钮
    market_btn_ele = (By.XPATH, '//span[@class="item-text" and text()="集市"]')

    # 首页欢迎字段
    huanying_ele = (By.XPATH, '//*[contains(text(),"欢迎来到")]')

    # 点击 “应用”按钮
    def click_app_btn(self):
        sleep(1)
        self.find_element_explicitly(self.app_btn_ele).click()

    # 点击 “数据”按钮
    def click_data_btn(self):
        sleep(1)
        self.find_element_explicitly(self.data_btn_ele).click()

    # 登录成功后的首页欢迎语
    def text_data_btn(self):
        self.find_element_explicitly(self.huanying_ele)
        print('登录成功')

    # 获取登录成功后的导航栏“数据”文本
    def get_text_of_data(self):
        return self.find_element_explicitly(self.data_btn_ele).text
