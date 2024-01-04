# -*- coding: utf-8 -*-
# @Time    : 2023/12/27 17:36
# @Author  : 居里夫人吃橘子
# @File    : check_data_object_business.py
# @Software: PyCharm
from src.common.parse_file import ParseFile
from src.pages.data.data_overview_page import DataOverviewPage
from src.pages.data.data_page import DataPage
from src.pages.other.home_page import HomePage


class CheckDataObjectBusiness(DataOverviewPage, HomePage, DataPage):

    def input_first_object_overview(self, case):
        '''
        进入第一个指定的数据对象
        :param case:
        :return:
        '''
        data = ParseFile('data', 'process_data.yaml').read_value_of_yaml(case)
        # 点击数据按钮》ui-test》指定数据集》指定的第一个数据对象
        self.click_data_btn()
        self.click_dirname_ele()
        self.click_setname_ele(data['data_set'])
        self.click_first_data_object(data['data_name'])

    def check_metadata_info(self, case):
        """
        检查元数据信息
        :param case:
        :return:
        """
        # 进入数据概览页面》点击元数据
        self.input_first_object_overview(case)
        self.click_metadata_btn()

    def check_data_content_info(self, case):
        """
        检查数据内容信息
        :param case:
        :return:
        """
        # 进入数据概览页面》点击数据内容
        self.input_first_object_overview(case)
        self.click_data_content_btn()
