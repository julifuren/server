import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.common.common_operation import common_operate_obj
from src.common.parse_csv import ParseCsv
import json
from os.path import abspath,dirname

#定义一个Base Page，用来封装 selenium 中的一些方法
class BasePage():

    def __init__(self, driver):
        self.driver = driver

    # 浏览器最大化，输入网址
    def open_url(self):
        self.driver.maximize_window()
        # 需要获取到 url
        url = ParseCsv("config", "url.csv").read_value_of_csv()["url_shouye"]
        # print(url)
        self.driver.get(url)



    # 使用显式等待 查找元素。
    def find_element_explicitly(self, locator, timeout=10, poll_frequency=0.5):
        """
        :param locator:          元素定位的表达式
        :param timeout:          查找元素的超时时间
        :param poll_frequency:   两次查找元素之间的间隔时间
        :return:                 返回定位到的元素
        """
        # 返回等待方法
        return WebDriverWait(self.driver, timeout, poll_frequency).until(
            expected_conditions.presence_of_element_located(locator))

    # 定义一个方法，用来实现 截图的操作。 截图整个屏幕。
    def get_screenshot(self, picture_name):
        # 获取 截图 的名称
        file_name = f"{picture_name}_{common_operate_obj.time_stamp()}.png"
        # 获取到 保存截图的路径
        picture_path = os.path.join(common_operate_obj.get_project_path(), "pictures", file_name)
        # 执行截图的操作
        self.driver.get_screenshot_as_file(picture_path)

    # 定义一个方法，用来实现 框架切换的操作。
    def switch_into_frame(self, frame, timeout=10, poll_frequency=0.5):
        WebDriverWait(self.driver, timeout, poll_frequency).until(expected_conditions.frame_to_be_available_and_switch_to_it(frame))

    # 定义一个方法，用来切换进入 父级框架 或者 默认框架。
    def switch_out_frame(self, frame_name):
        """
        :param frame_name: 表示要切换进入的框架，如果值为 parent， 则切换进入父级框架；
        如果值 为default，则切换进入默认框架。
        :return:
        """
        if frame_name == "parent":
            self.driver.switch_to.parent_frame()
        elif frame_name == "default":
            # 定义一个方法，用来 切换 进入默认框架。
            self.driver.switch_to.default_content()
        # 如果传入的值 不是 parent 、也不是 default ，则 抛出一个异常，提示 要切换进入的框架是不存在的。
        else:
            raise Exception("要切换的框架不存在，请确认！")

    # 定义一个方法， 用来实现选择 select标签 的下拉框中的选项
    def select_option(self, select_ele, visible_text):
        """
        :param select_ele:    表示的是定位到的 select 这个元素。
        :param visible_text:  表示的是下拉框中选项的文本内容。
        :return:
        """
        Select(select_ele).select_by_visible_text(visible_text)


if __name__ == '__main__':
    from selenium  import webdriver
    driver = webdriver.Chrome()
    test = BasePage(driver)
    test.open_url()

