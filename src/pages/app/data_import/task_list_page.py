# -*- coding: utf-8 -*-
# @Time : 2022/10/12 16:11
# @Author : 居里夫人吃橘子
# @Site : 
# @File : task_list_page.py
# @Software: PyCharm
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from src.pages.app.app_page import AppPage
from src.pages.base_page import BasePage
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage


class TaskListPage(BasePage):
    # 创建接入任务按钮
    create_task_btn_ele = (By.XPATH,'//div[@class="main-button-bottom"]//span[text()="创建接入任务"]')
    # 入库类型下拉框
    ruku_data_type_dropbox = (By.XPATH,'//form[@class="el-form"]//input')
    #文件存储设备
    storage_device = (By.XPATH,'//span[text()="NFS202208080"]')
    # 扫描目录按钮
    scan_dircetory_btn_ele = (By.CSS_SELECTOR,'[placeholder="请选择扫描的目录"] + [class="el-input-group__append"] [alt]')
    #选择扫描目录弹窗 确定 按钮
    scan_dircetory_popup_btn_ele = (By.XPATH,'//main[@class="el-main"]/div/div[3]/div[6]//span[text()="确 定"]')
    # 目标数据集按钮
    datasat_btn_ele =(By.CSS_SELECTOR,'[placeholder="请选择目标数据集"] + [class="el-input-group__append"] [alt]')
    # 数据集弹窗 “我的”
    datasat_popup_mysat_ele = (By.CSS_SELECTOR,'[id="tab-myDatas"]')




    # 点击创建接入任务
    def click_create_task_btn(self):
        self.find_element_explicitly(self.create_task_btn_ele).click()

    #选择入库类型
    def select_ruku_data_type_function(self,datatype):
        """
        选择入库类型时传入 数据类型 名称
        :param datatype: 数据类型参数名称
        :return:
        """
        self.find_element_explicitly(self.ruku_data_type_dropbox).click()
        # 参数化数据类型下拉框
        ruku_data_type_dropbox_value = (By.XPATH, '(//span[text()="{}"])[1]'.format(datatype))
        self.find_element_explicitly(ruku_data_type_dropbox_value).click()

    #选择测试数据路径
    def choose_data_path_function(self,data_filename,parent_file_name='Ui-test'):

        data_file_name11 = (By.XPATH, '//div[contains(@class,"middle-top")]//div[text()="{}"]'.format(data_filename))

        parent_file_name11 = (By.XPATH,'//div[@class="middle"]//div[text()="{}"]'.format(parent_file_name))

        self.find_element_explicitly(self.scan_dircetory_btn_ele).click()
        aa = self.find_element_explicitly(parent_file_name11)
        # 点击扫描目录按钮

        # 双击一级目录
        ActionChains(driver).double_click(aa).perform()
        self.find_element_explicitly(data_file_name11).click()
        self.find_element_explicitly(self.scan_dircetory_popup_btn_ele).click()

    #点击存储设备
    def click_storage_device(self):
        self.find_element_explicitly(self.storage_device).click()

    # 选择我的目录名 数据集名
    def choose_dataset_path_function(self,directory_name,mydatasat_name):
        """
        :param mydatasat_name: 我的数据集名称
        :return:
        """
        # 定位数据集按钮 滑动元素至可见
        ele = self.find_element_explicitly(self.datasat_btn_ele)
        hddatasat = ele.location_once_scrolled_into_view
        ele.click()

        #点击数据集弹窗 “我的” 页签
        self.find_element_explicitly(self.datasat_popup_mysat_ele).click()
        # self.driver.execute_script("arguments[0].click();", btn)

        # 定位目录名称 滑动元素至可见并双击
        dirname = (By.XPATH,'//div[@class="middle"]//div[text()="{}"]'.format(directory_name))
        aa = (self.find_element_explicitly(dirname))
        hdmydatasat_name = aa.location_once_scrolled_into_view
        ActionChains(driver).double_click(aa).perform()

        # 点击数据集
        satname = (By.XPATH,'//div[@class="middle"]//div[text()="{}"]'.format(mydatasat_name))
        self.find_element_explicitly(satname).click()















if __name__ == '__main__':
    from selenium import webdriver
    from src.common.parse_csv import ParseCsv

    driver = webdriver.Chrome()
    test = LoginPage(driver)
    username = ParseCsv("data", "login_data.csv").read_value_of_csv(2)[0]
    passwd = ParseCsv("data", "login_data.csv").read_value_of_csv(2)[1]
    print(username, passwd)
    test.open_url()
    test.login_function(username, passwd)
    HomePage(driver).click_app_btn()
    AppPage(driver).click_data_import_btn()
    test=TaskListPage(driver)
    test.click_create_task_btn()
    test.select_ruku_data_type_function('正射影像产品')
    test.click_storage_device()
    test.choose_data_path_function('region面84.zip')
    test.choose_dataset_path_function()

