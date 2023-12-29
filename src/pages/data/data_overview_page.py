# -*- coding: utf-8 -*-
# @Time    : 2023/12/27 17:08
# @Author  : 居里夫人吃橘子
# @File    : data_overview_page.py
# @Software: PyCharm
from time import sleep

from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from src.pages.data.data_page import DataPage


class DataOverviewPage(BasePage):
    # 地理位置信息文本
    geographical_position_text_ele = (By.XPATH, '//p[text()="地理位置"]/../p[2]')

    # 获取地理信息文字
    def get_geographical_position_text(self):

        for i in range(5):
            text = self.find_element_explicitly(self.geographical_position_text_ele).text
            if text == '暂无位置信息':
                sleep(1)
            else:
                return text


if __name__ == '__main__':
    from selenium import webdriver
    from src.pages.other.home_page import HomePage
    from src.business.other.login_business import LoginBusiness

    # 登录业务
    driver = webdriver.Chrome()
    BasePage(driver).open_url()
    LoginBusiness(driver).login_function('login_data.csv', 4)
    aa = DataPage(driver)
    aa.click_create_dir_btn()
    aa.input_dirname(2)
    aa.get_info_createset_prompt()
    # aa.click_create_dir_btn()
