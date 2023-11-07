# -*- coding: utf-8 -*-
# @Time    : 2022/12/30 15:05
# @Author  : 居里夫人吃橘子
# @File    : data_page.py
# @Software: PyCharm
from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.business.other.login_business import LoginBusiness
from src.pages.base_page import BasePage


class DataPage(BasePage):
    # 创建目录按钮
    create_dir_btn_ele = (By.XPATH, '//div[@class="nav-pic-box"]//img')
    # 目录名称输入框
    dirname_text_ele = (By.CSS_SELECTOR, '[placeholder="请输入目录名称"]')
    # 要检测的数据目录名称
    bb = (By.XPATH, '//span[text()="ui-test"]')
    # 创建数据集+按钮
    plus_btn_ele = (By.CSS_SELECTOR, '[class="edit-image"] [class="el-image__inner"]')
    # 创建数据集
    create_set_btn_ele = (By.XPATH, '//div[@class="popover-box"]//span[text()="创建数据集"]')
    # 数据集输入框
    setname_pop_text_ele = (By.CSS_SELECTOR, '[placeholder="数据集名称"]')
    # 创建按钮
    create_btn_ele = (By.XPATH, '//span[text()="创 建"]')
    # 点击创建后的提示信息
    create_set_prompt_info_ele = (By.CSS_SELECTOR, '[id="app"]~div :last-child')
    # 需要点击的数据目录
    dirname_ele = (By.XPATH, '//span[text()="ui-test"]/../../preceding-sibling::span')
    # 需要点击的数据集
    setname_ele = (By.XPATH, '//span[text()="矢量" and @class="dataset-span"]')
    # 导航栏添加数据图标
    add_data_icr_ele = (By.CSS_SELECTOR, '[class="btn-item"]:nth-child(2) [class="el-image el-tooltip"]')
    # 添加数据弹窗通过本地文件上传
    local_upload_ele = (By.XPATH, '//strong[text()="通过本地文件上传数据"]')
    # 文件上传区域
    file_upload_ele = (By.XPATH, '//em')
    # 添加数据弹窗中’导入‘
    import_btn_ele = (By.XPATH, '//span[text()="导 入"]')
    # 数据导入成功后提示信息
    import_success_text_ele = (By.XPATH, '//p[text()="入库成功"]')
    # 进度条100%
    progress_bar_text = (By.XPATH, '//div[text()="100%"]')
    # 导航栏任务列表按钮
    task_list_btn = (By.CSS_SELECTOR, '[class="el-image btn-img-click"] img')
    # 任务状态栏中的第一条数据任务状态
    first_task_statu_ele = (By.CSS_SELECTOR, '[class="status-card-list"]:nth-child(1) span')
    # 数据对象卡片
    data_object_ele = (By.XPATH, '//span[text()="region-GK"]')
    # 上传任务状态文本
    upload_text = (By.CSS_SELECTOR, '[class="init-store-status-text"]')

    # 矢量数据文件下拉框
    data_type_select = (By.XPATH, '//div[@class="upload-container"]/div/div[@class="flex-start"]')

    # 点击创建目录按钮
    def click_create_dir_btn(self):
        self.find_element_explicitly(self.create_dir_btn_ele).click()

    # 输入数据目录名称
    def input_dirname(self, dirname):
        self.find_element_explicitly(self.dirname_text_ele).send_keys(dirname)
        self.find_element_explicitly(self.dirname_text_ele).send_keys(Keys.ENTER)  # 回车

    # 判断指定的目录是否存在
    def dermines_ele_exist(self, dirname):
        dirname_text_ele = (By.XPATH, '//span[text()="{}"]'.format(dirname))
        return self.find_element_explicitly(dirname_text_ele, 2)

    # 点击创建数据集按钮
    def click_create_set_btn(self, hover_dirname):
        """
        :param hover_dirname:创建数据集时需要悬浮的数据目录名称
        :return:
        """
        # 创建数据集时悬浮的目录
        hover_dir_ele = (By.XPATH, '//span[text()="{}"]'.format(hover_dirname))
        ele = self.find_element_explicitly(hover_dir_ele)
        ActionChains(self.driver).move_to_element(ele).perform()
        self.find_element_explicitly(self.plus_btn_ele).click()
        self.find_element_explicitly(self.create_set_btn_ele).click()

    # 输入数据集名称
    def input_setname(self, setname):
        self.find_element_explicitly(self.setname_pop_text_ele).send_keys(setname)

    # 点击创建数据集弹窗中的“创建”
    def click_create_btn(self):
        self.find_element_explicitly(self.create_btn_ele).click()

    # 获取创建数据集成功后的提示信息
    def get_info_createset_prompt(self):
        ele = self.find_elements_explicitly(self.create_set_prompt_info_ele)[-1]

        return ele.text

    # 点击ui-test数据目录
    def click_dirname_ele(self):
        self.find_element_explicitly(self.dirname_ele).click()
        sleep(1)

    # 点击矢量数据集
    def click_setname_ele(self):
        self.find_element_explicitly(self.setname_ele).click()

    # 点击导航栏数据添加按钮
    def click_add_data_icr_ele(self):
        button = self.find_element_explicitly(self.add_data_icr_ele)
        ActionChains(self.driver).move_to_element(button).click(button).perform()

    # 点击通过本地文件上传数据
    def click_local_upload_ele(self):
        self.find_element_explicitly(self.local_upload_ele).click()

    # 点击上传文件区域
    def click_file_upload_ele(self):
        self.find_element_explicitly(self.file_upload_ele).click()

    # 点击弹窗的导入按钮
    def click_import_btn_ele(self):
        self.find_element_explicitly(self.import_btn_ele, 20).click()

    # 获取100%的进度条
    def get_progress_bar_text(self):
        aa = self.find_element_explicitly(self.progress_bar_text).text
        return aa

    # 获取任务状态
    def get_import_status(self):
        hover_ele = self.find_element_explicitly(self.task_list_btn)
        ActionChains(self.driver).move_to_element(hover_ele).perform()
        self.find_element_explicitly()

    # 获取数据对象卡片元素用于断言
    def get_data_object_ele(self):
        self.find_element_explicitly(self.data_object_ele, 30)

    # 监控上传任务弹窗状态
    def get_upload_text(self):
        # 先定位任务状态
        self.find_element_explicitly(self.upload_text)
        # 对任务状态监控直到消失
        self.find_not_element_explicity(self.upload_text)
        print('导入成功')

    def choose_data_type(self, data_type):
        self.find_element_explicitly(self.data_type_select).click()

        # 选择不同的类型
        data_type_to_xpath = {
            "影像或栅格文件": '//strong[text()="影像或栅格文件"]',
            "矢量数据文件": '//strong[text()=""矢量数据文件"]',
            "JSON格式矢量数据文件": '//strong[text()="//strong[text()="JSON格式矢量数据文件"]"]',
            "地理数据库文件": '//strong[text()="//strong[text()="地理数据库文件"]"]',
            "文档文件": '//strong[text()="//strong[text()="文档文件"]"]',
            "多媒体文件": '//strong[text()="//strong[text()="多媒体文件"]"]',
            "数字高程模型": '//strong[text()="//strong[text()="数字高程模型"]"]',
            "倾斜摄影模型": '//strong[text()="//strong[text()="倾斜摄影模型"]"]',
            "地图瓦片": '//strong[text()="//strong[text()="地图瓦片"]"]'
        }
        # 数据类型元素
        data_type_ele = (By.XPATH, data_type_to_xpath[data_type])

        # 点击指定的类型
        self.find_element_explicitly(data_type_ele).click()
        # ActionChains(self.driver).move_to_element(ele).perform()


if __name__ == '__main__':
    from selenium import webdriver
    from src.pages.other.home_page import HomePage

    # 登录业务
    driver = webdriver.Chrome()
    BasePage(driver).open_url()
    LoginBusiness(driver).login_function('login_data.csv', 4)
    aa = DataPage(driver)
    aa.click_create_dir_btn()
    aa.input_dirname(2)
    aa.get_info_createset_prompt()
    # aa.click_create_dir_btn()
