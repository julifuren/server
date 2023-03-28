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
from src.pages.other.home_page import HomePage
from src.pages.other.login_page import LoginPage
from src.common.parse_csv import ParseCsv


class TaskListPage(BasePage):
    # 创建接入任务按钮
    create_task_btn_ele = (By.XPATH, '//div[@class="main-button"]//span[text()="创建接入任务"]')
    # 入库类型下拉框
    ruku_data_type_dropbox = (By.XPATH,'//form[@class="el-form"]//input')
    # 任务名称
    task_name_ele = (By.XPATH,'//p[contains(text(),"任务名称")]/../..//input')
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
    # 数据集弹窗 “全部”
    datasat_popup_teamsat_ele = (By.CSS_SELECTOR, '[id="tab-teamDatas"]')
    # 数据集弹窗 "确定"
    datasat_popup_confirm_btn_ele = (By.XPATH,'//div[@class="configuration"]/div[5]//span[text()="确 定"]')
    # 下一步
    ruku_next_btn_ele = (By.XPATH,'//span[text()="下一步"]')

    # 获取创建任务后的任务 状态
    def get_ruku_status_text(self, taskname):
        """
        :param taskname:需要传入任务名称
        :return:
        """
        ruku_status_ele = (By.XPATH, '//div[contains(text(),"{}")]/../..//span[text()="完成"]'.format(taskname))
        ruku_fail_status_ele = (By.XPATH, '//div[contains(text(),"{}")]/../../td[9]//span'.format(taskname))

        # 120s内查找任务的状态为完成的字段，未查到直接返回当前状态
        try:
            aa = self.find_element_explicitly(ruku_status_ele, 120).text
            return aa
        except:
            bb = self.find_element_explicitly(ruku_fail_status_ele).text
            return bb

    # 点击创建接入任务
    def click_create_task_btn(self):
        self.find_element_explicitly(self.create_task_btn_ele).click()


    # 获取创建任务时的名称
    def get_taskname_text(self):
        return self.find_element_explicitly(self.task_name_ele).get_attribute('value')


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
    def choose_data_path_function(self,parent_file_name,son_file_name,data_filename):
        # 一级目录
        parent_file_name11 = (By.XPATH, '//div[@class="middle"]//div[text()="{}"]'.format(parent_file_name))
        # 二级目录
        son_file_name11 = (
        By.XPATH, '//div[@class="middle-top flex-space-between"]//div[text()="{}"]'.format(son_file_name))
        # 数据文件名
        data_file_name11 = (By.XPATH, '//div[@class="middle"]//div[text()="{}"]'.format(data_filename))

        # 点击扫描目录按钮
        scan_dircetory = self.find_element_explicitly(self.scan_dircetory_btn_ele)
        hdmydatasat_name = scan_dircetory.location_once_scrolled_into_view
        scan_dircetory.click()

        try:
            # 双击一级目录
            aa = self.find_element_explicitly(parent_file_name11)
            hdmydatasat_name = aa.location_once_scrolled_into_view
            ActionChains(self.driver).double_click(aa).perform()
        except BaseException:
            print("未找到{}一级目录".format(parent_file_name))
            raise

        try:
            # 双击二级目录
            bb = self.find_element_explicitly(son_file_name11)
            hdmydatasat_name1 = bb.location_once_scrolled_into_view
            ActionChains(self.driver).double_click(bb).perform()
        except BaseException:
            print("未找到{}二级目录".format(son_file_name))
            raise

        # 单击数据文件
        sleep(1)
        self.find_element_explicitly(data_file_name11).click()

        # 点击扫描目录弹窗确定按钮
        sleep(1)
        self.find_element_explicitly(self.scan_dircetory_popup_btn_ele).click()

    # 点击存储设备
    device_name = ParseCsv("config", 'device.csv').read_value_of_csv(1)['DeviceName']
    print(device_name)

    def click_storage_device(self, device_name):

        storage_device = (By.XPATH, '//span[text()="{}"]'.format(device_name))
        self.find_element_explicitly(storage_device).click()

    # 点击数据集弹窗 “我的” 页签
    def click_datasat_popup_mysat(self):
        # 定位数据集按钮 滑动元素至可见
        ele = self.find_element_explicitly(self.datasat_btn_ele)
        hddatasat = ele.location_once_scrolled_into_view
        ele.click()
        sleep(2)
        self.find_element_explicitly(self.datasat_popup_mysat_ele).click()
        sleep(2)

    # 点击数据集弹窗 “全部” 页签
    def click_datasat_popup_teamsat(self):
        # 定位数据集按钮 滑动元素至可见
        ele = self.find_element_explicitly(self.datasat_btn_ele)
        hddatasat = ele.location_once_scrolled_into_view
        ele.click()
        sleep(2)
        self.find_element_explicitly(self.datasat_popup_teamsat_ele).click()
        sleep(2)


    # 选择我的目录名 数据集名
    def choose_dataset_path_function(self,directory_name,mydataset_name):
        """
        :param mydataset_name: 我的数据集名称
        :return:
        """

        dirname = (By.XPATH,'//div[@class="middle"]//div[text()="{}"]'.format(directory_name))
        aa = (self.find_element_explicitly(dirname))
        hdmydatasat_name = aa.location_once_scrolled_into_view
        ActionChains(self.driver).double_click(aa).perform()

        # 点击数据集
        satname = (By.XPATH,'//div[@class="middle"]//div[text()="{}"]'.format(mydataset_name))
        self.find_element_explicitly(satname).click()

        sleep(1)
        self.find_element_explicitly(self.datasat_popup_confirm_btn_ele).click()

    # 点击下一步（入库界面）
    def click_ruku_next_btn(self):
        # sleep(1)
        self.find_element_explicitly(self.ruku_next_btn_ele).click()


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
    test = TaskListPage(driver)
    test.click_create_task_btn()
    aa = test.get_taskname_text()

    test.select_ruku_data_type_function('矢量要素数据')
    name = 'NFS-BuiltIn'
    test.click_storage_device(name)
    # test.click_datasat_popup_mysat()

    test.choose_data_path_function('ui-test', 'region面84.zip')
    test.click_datasat_popup_mysat()
    test.choose_dataset_path_function('ui-test', '矢量')
    test.click_ruku_next_btn()
    dd = test.get_ruku_status_text(aa)
    # print(dd)
