# -*- coding: utf-8 -*-
# @Time : 2022/3/18 15:27
# @Author : 居里夫人吃橘子
# @Site : 
# @File : type_management_page.py
# @Software: PyCharm
from time import sleep

from selenium.webdriver.common.by import By

from src.common.parse_csv import ParseCsv
from src.pages.base_page import BasePage


class TypeManagementPage(BasePage):
    # 类型管理按钮
    type_management_ele = (By.XPATH,'//span[text()="类型管理"]')
    # 定位卫星专题产品
    weixing_zhuanti_ele = (By.XPATH,'//p[text()="卫星专题产品" and @class="fonts" ]')
    # 定位 添加子类型 按钮
    add_son_type_btn = (By.XPATH,'//span[text()="添加子类型" ]')
    #创建子类型弹窗中的名称：输入框
    add_son_type_name_input_box = (By.CSS_SELECTOR,'[autocomplete="off"][type="text"]')

    # 添加子类弹窗中的‘确定’
    confim_btn = (By.XPATH,'//span[text()="确 定"]')
    #定位MODIS热异常和火灾产品
    # modis14_ele = (By.XPATH,'//span[text()="MODIS热异常和火灾产品"]')
    # modis14_ele = (By.XPATH, '//span[text()="MODIS叶面积指数产品"]')
    modis14_ele = (By.XPATH, '//span[text()="MODIS冰雪产品"]')

    #点击类型管理
    def click_type_management_ele(self):
        self.find_element_explicitly(self.type_management_ele).click()

    #点击卫星专题产品
    def click_weixing_zhuanti_ele(self):
        self.find_element_explicitly(self.weixing_zhuanti_ele).click()

    #点击MODIS热异常和火灾产品
    def click_modis14_ele(self):
        self.find_element_explicitly(self.modis14_ele).click()
    #点击添加子类型按钮
    def click_add_son_type_btn(self):
        self.find_element_explicitly(self.add_son_type_btn).click()
    #在 添加子类弹窗的输入框输入内容
    def send_keys_add_son_type_name_input_box(self,texts):
        self.find_element_explicitly(self.add_son_type_name_input_box).send_keys(texts)
    #点击创建子类型弹窗中的 确定 按钮
    def click_confim_btn(self):
        self.find_element_explicitly(self.confim_btn).click()




if __name__ == '__main__':
    from selenium import webdriver
    from src.pages.base_page import BasePage

    driver = webdriver.Chrome()
    test  =BasePage(driver)
    test.open_url()
    test.get_operation()
    type = TypeManagement(driver)
    type.click_type_management_lel()
    type.click_weixing_zhuanti_ele()
    type.click_modis14_ele()
    type.click_sort_type_select_ele()
