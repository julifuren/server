# -*- coding: utf-8 -*-
# @Time : 2022/10/17 16:31
# @Author : 居里夫人吃橘子
# @Site : 
# @File : login_business.py
# @Software: PyCharm

import os

from selenium.webdriver import ActionChains

from src.pages.other.home_page import HomePage
from src.pages.other.login_page import LoginPage
from src.common.parse_csv import ParseCsv


# 整合登录业务
class LoginBusiness(LoginPage, HomePage):
    project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    filename = project_path + '/' + 'business' + '/' + 'other' + '/' + 'cookies_file.json'

    def login_function(self, test_data_file, row):
        """

        :param test_data_file: 传入登录文件名
        :param row: 执行用例使用第几行的用户登录
        :return:
        """
        login_data = ParseCsv("data", test_data_file).read_value_of_csv(row)
        max_attempts = 3
        attempts = 0
        while attempts < max_attempts:

            try:

                # 调用登录方法
                self.login_server(login_data[0], login_data[1])
                self.get_text_of_data()
                break

            except:
                attempts += 1
                self.driver.refresh()

        if attempts == max_attempts:
            raise Exception("登录失败，已尝试登录{}次".format(max_attempts))


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    test = LoginBusiness(driver)
    test.open_url()
    test.login_function('login_data.csv', 2)
