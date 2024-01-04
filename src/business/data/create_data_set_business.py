# -*- coding: utf-8 -*-
# @Time    : 2023/3/29 15:33
# @Author  : 居里夫人吃橘子
# @File    : create_data_set_business.py
# @Software: PyCharm
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from src.common.parse_file import ParseFile
from src.pages.data.data_page import DataPage
from src.pages.other.home_page import HomePage


class CreateDataSetBusiness(DataPage, HomePage):

    def create_set(self, case):

        data = ParseFile('data', 'create_set.yaml').read_value_of_yaml()
        # 点击数据按钮
        self.click_data_btn()
        dirname = data[case]['data_dir']
        setname = data[case]['data_set']

        biaoshi = True
        # 判断指定的目录是否存在

        try:
            self.dermines_ele_exist(dirname)
            print('找到{}目录'.format(dirname))

        except TimeoutException:
            print('{}目录不存在'.format(dirname))
            biaoshi = False

        else:
            # 点击+号
            self.click_create_set_btn(dirname)
            self.input_setname(setname)
            self.click_create_btn()

        if not biaoshi:
            # 一级目录不存在进行创建一级目录
            self.click_create_dir_btn()
            self.input_dirname(dirname)
            print('创建一级目录{}成功'.format(dirname))

            # 再次进行创建数据集操作
            self.click_create_set_btn(dirname)
            self.input_setname(setname)
            self.click_create_btn()

        #
        print(self.get_info_createset_prompt())


if __name__ == '__main__':
    from src.business.other.login_business import LoginBusiness
    from selenium import webdriver
    from src.pages.base_page import BasePage
    from time import sleep

    dirver = webdriver.Chrome()
    BasePage(driver=dirver).open_url()
    LoginBusiness(dirver).login_function('login_data.csv', 4)
    aa = CreateDataSetBusiness(driver=dirver)
    aa.create_set('case1')
