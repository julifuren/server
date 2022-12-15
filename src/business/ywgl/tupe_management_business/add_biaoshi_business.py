# -*- coding: utf-8 -*-
# @Time : 2022/3/18 17:17
# @Author : 居里夫人吃橘子
# @Site :

# @Software: PyCharm
from time import sleep

from src.pages.ywgl.type_management.type_management_page import TypeManagementPage
from src.pages.ywgl.type_management.attribute_page import AttributePage
from src.common.parse_csv import ParseCsv
from src.pages.other.home_page import HomePage

class AddBiaoShi(TypeManagementPage,AttributePage):


    #定义一个方法实现添加标识信息 业务
    def add_type_management(self):

        HomePage(driver).click_operations_management_btn()

        #点击MODIS热异常和火灾产品
        self.click_modis14_ele()
        #点击标识信息下拉框
        self.click_sort_type_select_ele()
        sleep(1)
        #点击标识信息
        self.click_vlue_1()

    def input_infer(self,row):
        add_type_management_data = ParseCsv('data', 'biaoshi.csv').read_value_of_csv(row)
        # 编辑元数据 输入名称
        self.input_name_text_ele(add_type_management_data[0])
        sleep(0.5)
        # 编辑元数据 输入标题
        self.input_title_text_ele(add_type_management_data[1])
        sleep(0.5)
        # 点击类型下拉框
        self.click_type_select_ele()
        sleep(1)
        if add_type_management_data[2] == 'bytea':
            self.click_vlue_type_bytea()
        elif add_type_management_data[2] == 'int8':
            self.click_vlue_type_int8()
        elif add_type_management_data[2] == 'varchar':
            self.click_vlue_type_varchar()
        elif add_type_management_data[2] == 'float8':
            self.click_vlue_type_float8()
        elif add_type_management_data[2] == 'timestamp':
            self.click_vlue_type_timestamp()
        elif add_type_management_data[2] == 'int8':
            self.click_vlue_type_int8()
        else:
            print('field_type_name不存在')
        #判断是否需要点击扩展按钮
        if add_type_management_data[5] == 't':
            self.click_extent_btn()
        else:
            print('扩展属性不存在')

        if add_type_management_data[11] == 't':
            self.click_filter_btn()
        else:
            print('过滤属性不存在')

        # 点击添加元数据
        self.click_add_yuanshuju_btn()
        sleep(1)


if __name__ == '__main__':
    from src.pages.base_page import BasePage
    from selenium import webdriver
    driver = webdriver.Chrome()
    test = BasePage(driver)
    test.open_url()
    test.addcookies_login()

    test2 =AddBiaoShi(driver)
    test2.add_type_management()
    for row in range(2,22):
        test2.input_infer(row)
    driver.quit()





