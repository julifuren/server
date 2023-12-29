# -*- coding: utf-8 -*-
# @Time    : 2023/11/23 15:09
# @Author  : 居里夫人吃橘子
# @File    : service_page.py
# @Software: PyCharm
from time import sleep

from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class ServicePage(BasePage):
    # 服务 按钮
    service_btn_ele = (By.XPATH, '//span[@class="item-text" and text()="服务"]')

    # 我的 分组按钮
    my_btn_ele = (By.CSS_SELECTOR, '[id="tab-private"] span')
    # 第一个数据服务卡片
    first_service_object = (By.CSS_SELECTOR, '[class="new-service"] [class="new-service-datas"] ['
                                             'class="upload-content-card"]:first-child [class="data-card-thumbnail"]')

    # 图层展开按钮
    layer_unfold_btn = (By.CSS_SELECTOR, '[class="el-collapse-item service-item"]:first-child [class="el-image"] img')
    # 服务url
    service_url = (By.XPATH, '//div[contains(@class,"sib-url-info-input")]/input')

    #
    def click_my_first_server(self):
        self.find_element_explicitly(self.service_btn_ele).click()
        self.find_element_explicitly(self.my_btn_ele).click()
        sleep(1)
        self.find_element_explicitly(self.first_service_object).click()
        self.find_element_explicitly(self.layer_unfold_btn).click()

    def get_service_url_value(self):
        ele = self.find_elements_explicitly(self.service_url)[0]
        return ele.get_attribute('value')


if __name__ == '__main__':
    from selenium import webdriver
    from src.pages.other.home_page import HomePage
    from src.business.other.login_business import LoginBusiness

    # 登录业务
    driver = webdriver.Chrome()
    BasePage(driver).open_url()
    LoginBusiness(driver).login_function('login_data.csv', 3)
    aa = ServicePage(driver)
    aa.click_my_first_server()
    url = aa.get_service_url_value()
    new_url = url.replace('{y}', '12417').replace('{x}', '27009').replace('{z}', '15')
    # url.replace('{x}', '27009')
    # url.replace('{z}', '15')
    # print(type(url))
    # test = str(url)
    # test.replace()
    driver.get(new_url)
