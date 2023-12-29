# -*- coding: utf-8 -*-
# @Time    : 2023/12/27 17:36
# @Author  : 居里夫人吃橘子
# @File    : check_data_object_business.py
# @Software: PyCharm
from src.common.parse_file import ParseYaml
from src.pages.data.data_overview_page import DataOverviewPage
from src.pages.data.data_page import DataPage
from src.pages.other.home_page import HomePage


class CheckDataObjectBusiness(DataOverviewPage, HomePage, DataPage):

    def check_geography_info(self, case):
        data = ParseYaml('data', 'process_data.yaml').read_value_of_yaml()
        # 点击数据按钮
        self.click_data_btn()

        self.click_dirname_ele()

        self.click_setname_ele(data[case]['data_set'])

        # 点击第一个数据卡片
        self.click_first_data_object(data[case]['data_name'])
