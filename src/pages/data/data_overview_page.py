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
    # 成果名称
    result_name_ele = (By.XPATH, '//div[@title="成果名称"]//input')
    # 元数据按钮
    metadata_btn = (By.XPATH, '//div[text()="元数据"]')
    # 数据内容按钮
    data_content_btn = (By.XPATH, '//div[text()="数据内容"]')
    # 数据内容第一行第一列
    data_content_first_row = (By.CSS_SELECTOR, '[class="el-table__body-wrapper is-scrolling-none"] tbody '
                                               'tr:first-child td:nth-child(2) span')

    def get_geographical_position_text(self):
        '''
        获取地理信息文字
        :return:
        '''
        for i in range(5):
            text = self.find_element_explicitly(self.geographical_position_text_ele).text
            if text == '暂无位置信息':
                sleep(1)
            else:
                return text

    def get_metadata_result_text(self):
        """
        获取元数据中的成果名称
        :return:
        """
        return self.find_element_explicitly(self.result_name_ele).get_attribute('value')

    # 点击元数据按钮
    def click_metadata_btn(self):
        self.find_element_explicitly(self.metadata_btn).click()

    def get_content_first_row_text(self):
        """
        获取数据内容页的第一行的第一列文本
        :return:
        """
        return self.find_element_explicitly(self.data_content_first_row).text

    # 点击数据内容按钮
    def click_data_content_btn(self):
        self.find_element_explicitly(self.data_content_btn).click()


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
