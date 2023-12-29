# -*- coding: utf-8 -*-
# @Time    : 2023/11/10 17:03
# @Author  : 居里夫人吃橘子
# @File    : market_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class DataPage(BasePage):
    # 全局检索输入框
    global_search_input_box = (By.CSS_SELECTOR, '[placeholder="在此处发现数据"]')
