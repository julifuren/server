# -*- coding: utf-8 -*-
# @Time : 2022/10/17 16:31
# @Author : 居里夫人吃橘子
# @Site : 
# @File : login_business.py
# @Software: PyCharm
import json
import os
from time import sleep

from src.common.common_operation import CommonOperate

from src.pages.other.home_page import HomePage
from src.pages.other.login_page import LoginPage
from src.common.parse_csv import ParseCsv


# 整合登录业务，登录方法login_X根据实际业务定义
class LoginBusiness(LoginPage, HomePage):
    logindata = ParseCsv("data", "login_data.csv").read_value_of_csv(2)

    def login_judge(self, logway):
        """
        登录业务整合
        :param logway:"1"为验证码登录，“2”为无验证码登录
        :return:
        """
        if logway == '1':
            self.login_add_cookies(self.logindata[0], self.logindata[1])
        elif logway == '2':
            self.login_function(self.logindata[0], self.logindata[1])
        else:
            raise Exception

    # # 使用server账户登录
    # def login_2(self):
    #     logindata = ParseCsv("data", "login_data.csv").read_value_of_csv(2)
    #     self.login_function(logindata[0], logindata[1])
    #
    # # 使用租户管理员a123456账户登录
    # def login_3(self):
    #     logindata = ParseCsv("data", "login_data.csv").read_value_of_csv(3)
    #     self.login_function(logindata[0], logindata[1])
    #
    # # 使用租户管理员kk18821775875账户登录
    # def login_4(self):
    #     logindata = ParseCsv("data", "login_data.csv").read_value_of_csv(4)
    #     self.login_function(logindata[0], logindata[1])
    #
    # # 有验证码使用server账户cookies登录
    # def login_cookies(self):
    #     logindata = ParseCsv("data", "login_data.csv").read_value_of_csv(2)
    #     self.shoudong_login_function(logindata[0], logindata[1])

    # 使用cookies登录
    def login_add_cookies(self, user, pow):
        project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        filename = project_path + '/' + 'business' + '/' + 'other' + '/' + 'cookies_file.json'
        # print(filename)
        with open(filename, 'r') as cookies_file:
            test = json.load(cookies_file)
        self.open_url()
        for cookie in test:
            self.driver.add_cookie(cookie)
        self.open_url()

        # 定位登录后的数据文本
        try:
            self.text_data_btn()

        except:
            # 更新cookie并登录
            self.updata_cookie(user, pow)

    # 更新cookies文件
    def updata_cookie(self, username, password):
        self.login_cok_function(username=username, passwd=password)
        sleep(4)
        cks = self.driver.get_cookies()
        print('获取cookies成功')
        jsonCookies = json.dumps(cks)
        with open('cookies_file.json', 'w') as f:
            f.write(jsonCookies)
        print('更新cookies文件成功')


if __name__ == '__main__':
    from selenium import webdriver
    from src.common.parse_csv import ParseCsv

    driver = webdriver.Chrome()

    test = LoginPage(driver)
    test.open_url()
    LoginBusiness(driver).login_judge("1")

    # test = LoginBusiness(driver)
    # test.login_add_cookies()
