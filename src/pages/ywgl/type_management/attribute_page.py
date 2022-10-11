# -*- coding: utf-8 -*-
# @Time : 2022/3/31 15:20
# @Author : 居里夫人吃橘子
# @Site : 
# @File : attribute_page.py
# @Software: PyCharm
from time import sleep

from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class AttributePage(BasePage):
    # 定位添加按钮(添加类型的)
    add_bun = (By.XPATH, '//*[@class="flex-start"]/button/span')

    # 弹窗添加分类  输入框
    add_type_text_ele = (By.XPATH, '//*[@placeholder="请输入新的类别"]')

    # 添加分类  确定按钮
    add_type_confm_ele = (By.CSS_SELECTOR,'[aria-label="添加分类"] >[class="el-dialog__footer"] [class="el-button el-button--primary el-button--mini"]')

    # 类别下拉框
    type_sort_select_ele = (By.CSS_SELECTOR, '[class="flex-start"] [class="el-select el-select--mini"]')

    # 类别下拉框的  值   识别信息
    vlue_1 = (By.XPATH, '//span[text()="标识信息"]')
    vlue_2 = (By.XPATH, '//span[text()="覆盖信息"]')
    vlue_3 = (By.XPATH, '//span[text()="内容信息"]')
    vlue_4 = (By.XPATH, '//span[text()="传感器拍摄信息"]')


    #编辑元数据的  名称输入框
    name_text_ele=(By.CSS_SELECTOR,'[placeholder="Main data source"]')
    #编辑元数据的  标题输入框
    title_text_ele = (By.CSS_SELECTOR,'[placeholder="主要数据源"]')
    #编辑元数据的  类型下拉框
    type_select_ele = (By.CSS_SELECTOR,'[readonly="readonly"][placeholder="unknown"]')
    #编辑元数据的  类型下拉框值
    vlue_type_bytea= (By.XPATH,'//span[text()="bytea"]')
    vlue_type_bool = (By.XPATH, '//span[text()="bool"]')
    vlue_type_char = (By.XPATH, '//span[text()="char"]')
    vlue_type_data = (By.XPATH, '//span[text()="data"]')
    vlue_type_decimal = (By.XPATH, '//span[text()="decimal"]')
    vlue_type_float4 = (By.XPATH, '//span[text()="float4"]')
    vlue_type_float8 = (By.XPATH, '//span[text()="float8"]')
    vlue_type_int2 = (By.XPATH, '//span[text()="int2"]')
    vlue_type_int4 = (By.XPATH, '//span[text()="int4"]')
    vlue_type_int8 = (By.XPATH, '//span[text()="int8"]')
    vlue_type_json = (By.XPATH, '//span[text()="json"]')
    vlue_type_text = (By.XPATH, '//span[text()="text"]')
    vlue_type_timestamp = (By.XPATH, '//span[text()="timestamp"]')
    vlue_type_varchar = (By.XPATH, '//span[text()="varchar"]')
    vlue_type_geometry = (By.XPATH, '//span[text()="geometry"]')
    vlue_type_tsrange = (By.XPATH, '//span[text()="tsrange"]')
    vlue_type_varchararr = (By.XPATH, '//span[text()="varchararr"]')
    #编辑元数据的  是否可扩展单选按钮
    extent_btn = (By.CSS_SELECTOR,'[class="checkbox"]>div:nth-child(2)>label>span:first-child')
    #编辑元数据的  是否可过滤单选按钮
    filter_btn = (By.CSS_SELECTOR,'[class="checkbox"]>div:nth-child(3)>label>span:first-child')
    #编辑元数据的  中的添加按钮
    add_yuanshuju_btn = (By.CSS_SELECTOR,'[class="flex-space-between wrap"]>button:first-child')

    # 点击类型下拉框
    def click_type_select_ele(self):
        self.find_element_explicitly(self.type_select_ele).click()

    # 点击下拉框value_1
    def click_vlue_1(self):
        sleep(0.5)
        self.find_element_explicitly(self.vlue_1).click()

    # 点击下拉框value_2
    def click_vlue_2(self):
        self.find_element_explicitly(self.vlue_2).click()

    # 点击下拉框value_3
    def click_vlue_3(self):
        self.find_element_explicitly(self.vlue_3).click()

    # 点击下拉框value_4
    def click_vlue_4(self):
        self.find_element_explicitly(self.vlue_4).click()

    # 编辑元数据 中 名称输入
    def input_name_text_ele(self, name):
        self.find_element_explicitly(self.name_text_ele).send_keys(name)

    # 编辑元数据 中 标题输入
    def input_title_text_ele(self, title):
        self.find_element_explicitly(self.title_text_ele).send_keys(title)

    # 点击类型的下拉框
    def click_sort_type_select_ele(self):
        self.find_element_explicitly(self.type_sort_select_ele).click()

    # 点击类型下拉框中的值
    def click_vlue_type_bytea(self):
        self.find_element_explicitly(self.vlue_type_bytea).click()

    def click_vlue_type_bool(self):
        self.find_element_explicitly(self.vlue_type_bool).click()

    def click_vlue_type_char(self):
        self.find_element_explicitly(self.vlue_type_char).click()

    def click_vlue_type_data(self):
        self.find_element_explicitly(self.vlue_type_data).click()

    def click_vlue_type_decimal(self):
        self.find_element_explicitly(self.vlue_type_decimal).click()

    def click_vlue_type_float4(self):
        self.find_element_explicitly(self.vlue_type_float4).click()

    def click_vlue_type_float8(self):
        self.find_element_explicitly(self.vlue_type_float8).click()

    def click_vlue_type_int2(self):
        self.find_element_explicitly(self.vlue_type_int2).click()

    def click_vlue_type_int4(self):
        self.find_element_explicitly(self.vlue_type_int4).click()

    def click_vlue_type_int8(self):
        self.find_element_explicitly(self.vlue_type_int8).click()

    def click_vlue_type_json(self):
        self.find_element_explicitly(self.vlue_type_json).click()

    def click_vlue_type_text(self):
        self.find_element_explicitly(self.vlue_type_text).click()

    def click_vlue_type_timestamp(self):
        self.find_element_explicitly(self.vlue_type_timestamp).click()

    def click_vlue_type_varchar(self):
        self.find_element_explicitly(self.vlue_type_varchar).click()

    def click_vlue_type_geometry(self):
        self.find_element_explicitly(self.vlue_type_geometry).click()

    def click_vlue_type_tsrange(self):
        self.find_element_explicitly(self.vlue_type_tsrange).click()

    def click_vlue_type_varchararr(self):
        self.find_element_explicitly(self.vlue_type_varchararr).click()

    # 点击扩展按钮
    def click_extent_btn(self):
        self.find_element_explicitly(self.extent_btn).click()

    # 点击过滤按钮
    def click_filter_btn(self):
        self.find_element_explicitly(self.filter_btn).click()

    # 点击添加按钮
    def click_add_yuanshuju_btn(self):
        self.find_element_explicitly(self.add_yuanshuju_btn).click()