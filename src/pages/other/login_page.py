# -*- coding: utf-8 -*-
# @Time : 2022/10/12 14:59
# @Author : 居里夫人吃橘子
# @Site : 
# @File : login_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
# 未登录页面
class LoginPage(BasePage):
    # 未登录页面 ‘登录’按钮
    login_btn = (By.XPATH,'//div[text()="登录"]')
    # 用户名输入框
    username_input_box_ele = (By.CSS_SELECTOR,'[id="input-1"]')
    # 密码输入框
    passwd_input_box_ele = (By.CSS_SELECTOR, '[id="input-3"]')
    # 登录按钮
    logined_btn = (By.CSS_SELECTOR, '[id="agreement"]')

    # 登录方法
    def login_function(self, username, passwd):
        self.find_element_explicitly(self.login_btn).click()
        self.find_element_explicitly(self.username_input_box_ele).send_keys(username)
        self.find_element_explicitly(self.passwd_input_box_ele).send_keys(passwd)
        self.find_element_explicitly(self.logined_btn).click()

    # 登录页面有验证码
    def shoudong_login_function(self, username, passwd):
        self.find_element_explicitly(self.login_btn).click()
        self.find_element_explicitly(self.username_input_box_ele).send_keys(username)
        self.find_element_explicitly(self.passwd_input_box_ele).send_keys(passwd)
        input("请输入验证码后按回车")
        self.find_element_explicitly(self.logined_btn).click()

if __name__ == '__main__':
    from selenium import webdriver
    from src.common.parse_csv import ParseCsv
    driver = webdriver.Chrome()
    test = LoginPage(driver)
    username = ParseCsv("data","login_data.csv").read_value_of_csv(2)[0]
    passwd = ParseCsv("data","login_data.csv").read_value_of_csv(2)[1]
    print(username,passwd)
    test.open_url()
    test.login_function(username,passwd)

