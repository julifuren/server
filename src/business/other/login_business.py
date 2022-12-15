# -*- coding: utf-8 -*-
# @Time : 2022/10/17 16:31
# @Author : 居里夫人吃橘子
# @Site : 
# @File : login_business.py
# @Software: PyCharm


from src.pages.other.login_page import LoginPage
from src.common.parse_csv import ParseCsv
# 整合登录业务
class LoginBusiness(LoginPage):
    # 实现登录方法
    def login(self):
        logindata = ParseCsv("data", "login_data.csv").read_value_of_csv(2)
        self.login_function(logindata[0], logindata[1])

    # 获取cookies，分支测试
    def get_cookies_vule(self):
        self.login()


if __name__ == '__main__':
    from selenium import webdriver
    from src.common.parse_csv import ParseCsv

    driver = webdriver.Chrome()
    test = LoginPage(driver)
    test.open_url()
    LoginBusiness(driver).login()
