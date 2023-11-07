# -*- coding: utf-8 -*-
# @Time : 2022/3/18 15:07
# @Author : 居里夫人吃橘子
# @Site : 
# @File : common_operation.py
# @Software: PyCharm
import os
import time
import warnings
# 这里只能导入的是模块。不能直接导入 该模块（parse_csv.py）中的类。
from src.common import parse_csv
# python自带的插件，win32api是用来模拟键盘操作
import win32api
# python自带的插件，win32con是用来控制键盘
import win32con
# 脚本字段的复制、粘贴
import pyperclip


# 定义一个类，用来实现 通用的操作。 获取 工程所在的目录、获取系统当前时间的功能
class CommonOperate():

    # 定义一个方法，用来实现获取工程目录的功能
    def get_project_path(self):
        return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # 定义一个方法，用来实现获取系统当前的时间。 年月日时分秒   24 小时制
    def time_stamp(self):
        return time.strftime("%Y%m%d_%H_%M_%S")

    def isnot_input_uploadfile(self, eleLoc, filePath, doc=''):
        """
        使用python的win32api,win32con模拟按键输入,实现文件上传操作
        :param eleLoc: 页面中的上传文件按钮
        :param filePath: 要上传的文件地址(绝对路径)
        :param doc: 备注信息
        :return:
        """
        # 复制文件路径到剪切板（需要上传文件的绝对路径）
        pyperclip.copy(filePath)
        # # 点击上传文件按钮
        # self.find_element_explicitly(eleLoc).click()
        # time.sleep(3)
        # 将剪切的内容粘贴（Ctrl+V）
        win32api.keybd_event(17, 0, 0, 0)
        win32api.keybd_event(86, 0, 0, 0)
        # 松开按键
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)
        # 点击回车键
        win32api.keybd_event(13, 0, 0, 0)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(2)


# 为了避免多次实例化占用内存空间，可以提前实例化一个对象出来。只需要在这里实例化一次即可。
common_operate_obj = CommonOperate()

if __name__ == '__main__':
    print(CommonOperate().get_project_path())
    print(CommonOperate().time_stamp())
    # sql = 'SELECT password FROM stfoa.`oa_tbl_employee` WHERE loginid = "fuc";'
    # print(common_operate_obj.execute_sql(sql)[0][0])
