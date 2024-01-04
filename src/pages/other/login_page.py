# -*- coding: utf-8 -*-
# @Time : 2022/10/12 14:59
# @Author : 居里夫人吃橘子
# @Site : 
# @File : login_page.py
# @Software: PyCharm
from time import sleep

from selenium.webdriver.common.by import By

from src.common.yanzheng import parse_yanzheng
from src.pages.base_page import BasePage


# 未登录页面
class LoginPage(BasePage):
    # 未登录页面 ‘登录’按钮
    login_btn = (By.XPATH, '//div[text()="登录"]')
    # 用户名输入框
    username_input_box_ele = (By.CSS_SELECTOR, '[id="input-1"]')
    # 密码输入框
    passwd_input_box_ele = (By.CSS_SELECTOR, '[id="input-3"]')
    # 验证码输入框
    yanzheng_input_box_ele = (By.CSS_SELECTOR, '[id="input-2"]')
    # 登录按钮
    logined_btn = (By.CSS_SELECTOR, '[id="agreement"]')

    # 封装登录-有验证码
    def login_server(self, username, passwd):
        self.find_element_explicitly(self.username_input_box_ele).send_keys(username)
        self.find_element_explicitly(self.passwd_input_box_ele).send_keys(passwd)
        yanzhegnma = parse_yanzheng()
        self.find_element_explicitly(self.yanzheng_input_box_ele).send_keys(yanzhegnma)
        self.find_element_explicitly(self.logined_btn).click()

    # 封装登录-私有化无验证码
    def login_syh(self, username, passwd):
        self.find_element_explicitly(self.username_input_box_ele).send_keys(username)
        self.find_element_explicitly(self.passwd_input_box_ele).send_keys(passwd)
        self.find_element_explicitly(self.logined_btn).click()

if __name__ == '__main__':
    from selenium import webdriver
    from src.common.parse_file import ParseFile

    driver = webdriver.Chrome()
    test = LoginPage(driver)
    username = ParseFile("data", "login_data.csv").read_value_of_csv(2)[0]
    passwd = ParseFile("data", "login_data.csv").read_value_of_csv(2)[1]
    print(username, passwd)
    test.open_url()
    test.login_server(username, passwd)
