# -*- coding: utf-8 -*-
# @Time : 2022/3/31 18:24
# @Author : 居里夫人吃橘子
# @Site : 
# @File : get_cookies.py
# @Software: PyCharm
import json
from time import sleep

from selenium.webdriver.common.by import By

from src.business.other.login_business import LoginBusiness
from src.pages.base_page import BasePage
from selenium import webdriver

from src.pages.other.login_page import LoginPage


class GetCookies(LoginBusiness):

    def log(self):
        self.shoudong_login()
        sleep(4)
        cks = self.driver.get_cookies()
        print('获取cookies成功')
        jsonCookies = json.dumps(cks)
        with open('cookies_file.json', 'w') as f:
            f.write(jsonCookies)
        print('更新cookies文件成功')
        self.driver.quit()

    def read_jsonfile(self):
        filename = 'cookies_file.json'
        with open(filename, 'r') as cookies_file:
            test = json.load(cookies_file)
            print(test)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    test = GetCookies(driver)
    test.open_url()
    test.log()
    # GetCookies(driver).read_jsonfile()
