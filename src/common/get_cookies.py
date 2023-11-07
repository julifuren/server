# -*- coding: utf-8 -*-
# @Time : 2022/3/31 18:24
# @Author : 居里夫人吃橘子
# @Site : 
# @File : get_cookies.py
# @Software: PyCharm
import json
from time import sleep
from src.business.other.login_business import LoginBusiness
from selenium import webdriver



class GetCookies(LoginBusiness):

    def log(self, username, password):
        self.login_cok_function(username=username, passwd=password)
        self.sleep = sleep(4)
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
    test.log('18729966516', '123456')
    # GetCookies(driver).read_jsonfile()
