# -*- coding: utf-8 -*-
# @Time : 2022/3/31 18:24
# @Author : 居里夫人吃橘子
# @Site : 
# @File : get_cookies.py
# @Software: PyCharm
import json
from time import sleep

from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from selenium import webdriver
# 成功登录的
driver =webdriver.Chrome()
class GetCookies(BasePage):
    driver.get('https://cloudtest.piesat.cn/sso/account-login?ReturnUrl=https%3A%2F%2Fcloudtest.piesat.cn%2Fengine-server-test%2F&clientId=2231c8b20ba04bdc90590cd19225239b')
    name = (By.CSS_SELECTOR,'[type="text"][id="input-1"]')
    pwd = (By.CSS_SELECTOR,'[placeholder="登录密码"]')
    config_btn = (By.CSS_SELECTOR,'[id="agreement"]')

    def login(self):
        self.find_element_explicitly(self.name).send_keys('17729546158')
        self.find_element_explicitly(self.pwd).send_keys('123456')


        input("输入验证码后敲回车")
        self.find_element_explicitly(self.config_btn).click()
        sleep(4)
        cks = driver.get_cookies()
        jsonCookies = json.dumps(cks)
        with open('cookies_file.json', 'w') as f:
            f.write(jsonCookies)
    def read_jsonfile(self):
        filename = 'cookies_file.json'
        with open(filename,'r') as cookies_file:
            test  = json.load(cookies_file)
            print(test)
if __name__ == '__main__':
    GetCookies(driver).login()
    # GetCookies(driver).read_jsonfile()