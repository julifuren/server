# -*- coding: utf-8 -*-
# @Time    : 2023/11/17 10:53
# @Author  : 居里夫人吃橘子
# @File    : login_test.py
# @Software: PyCharm


import unittest

from selenium import webdriver


class LoginTest(unittest.TestCase):
    driver = webdriver.Chrome()

    def setUp(self) -> None:
        driver = webdriver.Chrome()

    def test_01(self):
