# -*- coding: utf-8 -*-
# @Time : 2022/10/17 16:49
# @Author : 居里夫人吃橘子
# @Site : 
# @File : create_datatask_business.py
# @Software: PyCharm
from time import sleep

from src.pages.app.app_page import AppPage
from src.pages.app.data_import.task_list_page import TaskListPage
from src.pages.other.home_page import HomePage
from src.common.parse_csv import ParseCsv


class CreateDatataskBusiness(TaskListPage,AppPage,HomePage):

    task_name = 'ab'
    def create_datatask(self,row):

        # 解析入库数据文件
        data_task = ParseCsv("data","ruku_data_task.csv").read_value_of_csv(row)
        # 点击应用按钮
        self.click_app_btn()
        # 点击数据导入
        self.click_data_import_btn()
        sleep(2)
        # 点击创建入库任务
        self.click_create_task_btn()
        #声明task_name为全局参数
        global task_name
        task_name = self.get_taskname_text()

        # 选择入库数据类型
        self.select_ruku_data_type_function(data_task[0])
        device_name = ParseCsv("config", 'device.csv').read_value_of_csv(1)['DeviceName']
        # 点击存储设备
        self.click_storage_device(device_name)

        # 选择数据目录路径
        self.choose_data_path_function(data_task[1],data_task[2],data_task[3])

        if data_task[4] == "我的":
            self.click_datasat_popup_mysat()
        elif data_task[4] == "全部":
            self.click_datasat_popup_teamsat()
        else:
            raise Exception("无{}数据集分组，请重新选择".format(data_task[4]))

        # 选择数据集路径
        self.choose_dataset_path_function(data_task[5],data_task[6])

        self.click_ruku_next_btn()

        # status = self.get_ruku_status_text(task_name)

    #定义一个方法用判断创建后的任务执行状态
    def assert_taskname_text(self):
        dd = task_name
        return self.get_ruku_status_text(dd)






if __name__ == '__main__':
    from selenium import webdriver
    from src.business.other.login_business import LoginBusiness
    from selenium.webdriver.common.by import By
    driver = webdriver.Chrome()

    test = LoginBusiness(driver)
    test.open_url()
    test.login()

    cc = CreateDatataskBusiness(driver)
    cc.create_datatask(2)
    vv = cc.taskname_text()
    print(vv)

    # driver.find_element(By.XPATH,'//div[contains(text(),"OldShuRoadAll.zip") and (@class="cell el-tooltip")]/../..//span[@class="el-tag el-tag--success el-tag--light"]')
    # aa.create_datatask(2)









