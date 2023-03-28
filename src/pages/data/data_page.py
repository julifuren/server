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
from src.common.parse_csv import ParseCsv
from src.pages.base_page import BasePage
from src.pages.other.home_page import HomePage


class DataPage(BasePage):
    # 创建目录按钮
    create_dir_btn_ele = (By.XPATH, '//div[@class="nav-pic-box"]//img')
    # 目录名称输入框
    dirname_ele = (By.CSS_SELECTOR, '[placeholder="请输入目录名称"]')
    # 要检测的数据目录名称
    bb = (By.XPATH, '//span[text()="ui-test"]')
    # 创建数据集时悬浮的目录
    hover_dir_ele = (By.XPATH, '//span[text()="ui-test"]')
    # 创建数据集+按钮
    plus_btn_ele = (By.CSS_SELECTOR, '[class="edit-image"] [class="el-image__inner"]')
    # 创建数据集
    create_set_btn_ele = (By.XPATH, '//div[@class="popover-box"]//span[text()="创建数据集"]')
    # 数据集输入框
    setname_pop_text_ele = (By.CSS_SELECTOR, '[placeholder="数据集名称"]')
    # 创建按钮
    create_btn_ele = (By.XPATH, '//span[text()="创 建"]')
    # 点击创建后的提示信息
    create_set_prompt_info_ele = (By.XPATH, '//p[text()="新建数据集成功"]')

    # 点击创建目录按钮
    def click_create_dir_btn(self):
        self.find_element_explicitly(self.create_dir_btn_ele).click()

    # 输入数据目录名称
    def input_dirname(self, row):
        # 解析创建
        self.dir_name = ParseCsv("data", "create_dir_name.csv").read_value_of_csv(row)

        try:
            bb = (By.XPATH, '//span[text()="{}"]'.format(self.dir_name[0]))
            self.find_element_explicitly(bb, 2)
            # print('已存在{}目录'.format(self.dir_name))

        except:
            self.find_element_explicitly(self.create_dir_btn_ele).click()
            self.find_element_explicitly(self.dirname_ele).send_keys(self.dir_name[0])
            self.find_element_explicitly(self.dirname_ele).send_keys(Keys.ENTER)
        else:
            raise Exception('已存在{}目录'.format(self.dir_name))

    def input_setname(self, row):
        ele = self.find_element_explicitly(self.hover_dir_ele)
        ActionChains(driver).move_to_element(ele).perform()
        self.find_element_explicitly(self.plus_btn_ele)


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    BasePage(driver).open_url()
    LoginBusiness(driver).login_2()
    HomePage(driver).click_data_btn()
    aa = DataPage(driver)
    aa.input_dirname(2)
    # aa.click_create_dir_btn()
