# -*- coding: utf-8 -*-
# @Time    : 2022/12/30 15:05
# @Author  : 居里夫人吃橘子
# @File    : data_page.py
# @Software: PyCharm
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.business.other.login_business import LoginBusiness
from src.pages.base_page import BasePage


class DataPage(BasePage):
    # 创建目录按钮
    create_dir_btn_ele = (By.XPATH, '//div[@class="nav-pic-box"]//img')
    # 目录名称输入框
    dirname_text_ele = (By.CSS_SELECTOR, '[placeholder="请输入目录名称"]')
    # 要检测的数据目录名称
    bb = (By.XPATH, '//span[text()="ui-test"]')

    # 创建数据集+按钮
    plus_btn_ele = (By.CSS_SELECTOR, '[class="edit-image"] [class="el-image__inner"]')
    # 创建数据集
    create_set_btn_ele = (By.XPATH, '//div[@class="popover-box"]//span[text()="创建数据集"]')
    # 数据集输入框
    setname_pop_text_ele = (By.CSS_SELECTOR, '[placeholder="数据集名称"]')
    # 创建按钮
    create_btn_ele = (By.XPATH, '//span[text()="创 建"]')
    # 点击创建后的提示信息
    create_set_prompt_info_ele = (By.CSS_SELECTOR, '[id="app"]~div :last-child')

    # create_set_prompt_info_ele = (By.XPATH,'//div[contains(@class,"el-message--warning")]')

    # 点击创建目录按钮
    def click_create_dir_btn(self):
        self.find_element_explicitly(self.create_dir_btn_ele).click()

    # 输入数据目录名称
    def input_dirname(self, dirname):
        self.find_element_explicitly(self.dirname_text_ele).send_keys(dirname)
        self.find_element_explicitly(self.dirname_text_ele).send_keys(Keys.ENTER)  # 回车

    # 判断指定的目录是否存在
    def dermines_ele_exist(self, dirname):
        dirname_text_ele = (By.XPATH, '//span[text()="{}"]'.format(dirname))
        return self.find_element_explicitly(dirname_text_ele, 2)

    # 点击创建数据集按钮
    def click_create_set_btn(self, hover_dirname):
        """
        :param hover_dirname:创建数据集时需要悬浮的数据目录名称
        :return:
        """
        # 创建数据集时悬浮的目录
        hover_dir_ele = (By.XPATH, '//span[text()="{}"]'.format(hover_dirname))
        ele = self.find_element_explicitly(hover_dir_ele)
        ActionChains(self.driver).move_to_element(ele).perform()
        self.find_element_explicitly(self.plus_btn_ele).click()
        self.find_element_explicitly(self.create_set_btn_ele).click()

    # 输入数据集名称
    def input_setname(self, setname):
        self.find_element_explicitly(self.setname_pop_text_ele).send_keys(setname)

    # 点击创建数据集弹窗中的“创建”
    def click_create_btn(self):
        self.find_element_explicitly(self.create_btn_ele).click()

    # 获取创建数据集成功后的提示信息
    def get_info_createset_prompt(self):
        ele = self.find_elements_explicitly(self.create_set_prompt_info_ele)[-1]

        return ele.text


if __name__ == '__main__':
    from selenium import webdriver
    from src.pages.other.home_page import HomePage

    driver = webdriver.Chrome()
    BasePage(driver).open_url()
    LoginBusiness(driver).login_2()
    HomePage(driver).click_data_btn()
    aa = DataPage(driver)
    aa.click_create_dir_btn()
    aa.input_dirname(2)
    aa.get_info_createset_prompt()
    # aa.click_create_dir_btn()
