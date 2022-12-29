# -*- coding: utf-8 -*-
# @Time : 2022/10/17 16:31
# @Author : 居里夫人吃橘子
# @Site : 
# @File : login_business.py
# @Software: PyCharm
import json
import os

from src.common.common_operation import CommonOperate
from src.pages.other.login_page import LoginPage
from src.common.parse_csv import ParseCsv


# 整合登录业务
class LoginBusiness(LoginPage):

    # 实现登录方法
    def login(self):
        logindata = ParseCsv("data", "login_data.csv").read_value_of_csv(2)
        self.login_function(logindata[0], logindata[1])

<<<<<<< HEAD
    # 获取cookies，分支测试
    def get_cookies_vule(self):
        self.login()
=======
    # 有验证码获取cookies时登录
    def shoudong_login(self):
        logindata = ParseCsv("data", "login_data.csv").read_value_of_csv(2)
        self.shoudong_login_function(logindata[0], logindata[1])

    # 使用cookies登录
    def login_add_cookies(self):
        project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        filename = project_path + '/' + 'common' + '/' + 'cookies_file.json'
        print(filename)
        with open(filename, 'r') as cookies_file:
            test = json.load(cookies_file)
        self.open_url()
        for cookie in test:
            self.driver.add_cookie(cookie)
        self.open_url()
>>>>>>> master


if __name__ == '__main__':
    from selenium import webdriver
    from src.common.parse_csv import ParseCsv

    driver = webdriver.Chrome()
<<<<<<< HEAD
    test = LoginPage(driver)
    test.open_url()
    LoginBusiness(driver).login()
=======
    test = LoginBusiness(driver)
    test.login_add_cookies()
>>>>>>> master
