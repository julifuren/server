# -*- coding: utf-8 -*-
# @Time : 2022/3/31 15:33
# @Author : 居里夫人吃橘子
# @Site : 
# @File : add_son_type_business.py
# @Software: PyCharm
#用于添加子类型业务
from selenium import webdriver

from src.common.parse_file import ParseFile
from src.pages.ywgl.type_management.type_management_page import TypeManagementPage

class AddSonTypeBusiness(TypeManagementPage):

    #点击添加子类型业务并保存
    def add_son_type_btn_business(self,row):
        # 点击 类型管理 页签
        son_type_english_name = ParseFile('data', 'sontype.csv').read_value_of_csv(row)[0]
        print(son_type_english_name)
        self.click_type_management_ele()
        # 点击卫星专题产品
        self.click_weixing_zhuanti_ele()
        #点击添加子类型
        self.click_add_son_type_btn()
        #在创建子类型弹窗中 输入 名称
        self.send_keys_add_son_type_name_input_box(son_type_english_name)
        #点击确定
        self.click_confim_btn()


if __name__ == '__main__':
    from src.pages.base_page import BasePage

    driver = webdriver.Chrome()
    test = BasePage(driver)
    test.open_url()
    test.get_operation()

    aa =AddSonTypeBusiness(driver).add_son_type_btn_business(2)