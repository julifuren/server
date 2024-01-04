# -*- coding: utf-8 -*-
# @Time    : 2023/6/21 15:45
# @Author  : 居里夫人吃橘子
# @File    : upload_data_business.py
# @Software: PyCharm
# -*-coding:utf-8;-*-
import time
from src.business.other.login_business import LoginBusiness
from src.common.common_operation import common_operate_obj, CommonOperate
from src.common.parse_file import ParseFile
from selenium.webdriver.common.by import By
from src.pages.data.data_page import DataPage
from src.pages.other.home_page import HomePage
from src.pages.other.login_page import LoginPage


class UploadDataBusiness(DataPage, HomePage):

    # 上传数据业务
    def uploaddata(self, row, timeout=5):
        """
        仅用于数据上传业务，传入的数据文件格式为CSV
        :param row: csv文件中的第几行
        :param file_name: 数据上传的文件数据名
        :param timeout: 监测100%进度条的超时时间，默认5s

        :return:
        """

        # 解析上传的文件数据
        upload_data = ParseFile("data", 'upload_data.csv').read_value_of_csv(row)
        # 上传文件路径
        file_wenjian = common_operate_obj.get_project_path() + '\\files' + '\\' + upload_data[0] + '\\' + upload_data[1]

        self.click_data_btn()
        self.click_dirname_ele()

        # 选择需要上传的数据集名称
        self.click_setname_ele(upload_data[2])

        self.click_add_data_icr_ele()

        # 点击通过本地上传
        self.click_local_upload_ele()

        # 选择类型
        self.choose_data_type(upload_data[0])
        time.sleep(1)

        # 点击通过文件上传区域
        self.click_file_upload_ele()
        time.sleep(2)

        # common_operate_obj.uploadWinFile(filepath=file_wenjian)

        # 非input文件上传
        common_operate_obj.isnot_input_uploadfile(self.file_upload_ele, file_wenjian)

        # 校验文件是否加载成功
        self.get_upload_file_status()

        # 点击导入按钮
        self.click_import_btn_ele()

        # 获取上传数据的进度条为100%，需传入指定时间
        self.get_progress_bar_text(timeout)

    def get_task_status(self):
        """

        :param timeout: 数据导入的超时时间
        :return:
        """
        self.get_upload_text()


if __name__ == '__main__':
    from selenium import webdriver

    upload_data = ParseFile('data', 'upload_data.csv').read_value_of_csv(2)
    # 登录业务
    driver = webdriver.Chrome()

    LoginPage(driver).open_url()
    LoginBusiness(driver).login_function('login_data.csv', 4)
    aa = UploadDataBusiness(driver)

    file_upload_ele = (By.XPATH, '//em')
    # files = 'C:\\Users\\11361\\Desktop\测试数据\\1.矢量数据文件\\region-GK.zip'

    # files = 'C:\\Users\\11361\\Desktop\测试数据\\2.影像或栅格文件\\道路1706_前_2000.zip'

    aa.uploaddata(2)
    aa.get_task_status()
