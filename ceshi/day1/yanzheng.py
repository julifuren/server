# -*- coding: utf-8 -*-
# @Time    : 2023/10/8 15:03
# @Author  : 居里夫人吃橘子
# @File    : yanzheng.py
# @Software: PyCharm
import requests
import ddddocr

# 定义接口URL
url = 'https://janus.piesat.cn/gateway/api'  # 替换成你的接口URL

# 如果需要传递POST请求的数据，可以在这里定义
payload = {'action': 'PWDLOGIN', 'sendType': 'WEB'}  # 根据需要添加POST请求的数据
# 定义请求头
headers = {

    'x-api': 'engine.login.getGraphCaptcha',
    'x-app': 'rPvyWAC0cvfT66TH1UbO',
    'x-client': 'WEB',
    'x-gw-version': '2',
    'x-host-app-id': 'engine',
    'x-language': 'zh_CN',
    'x-nonce': '99a14f90-bb3a-4099-a191-a9fadd4b2756',
    'x-sign': 'd8f4e2a9080b4e1aa8306d6ec521d784',
    'x-stage': 'PROD',
    'x-ts': '1696748451856',
}
# 发送POST请求
response = requests.post(url, json=payload, headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    # 获取图片内容
    image_data = response.content

    # 指定保存的文件名和路径
    filename = 'downloaded_image.jpg'  # 可以根据需要修改文件名和扩展名

    # 使用二进制写入模式保存图片
    with open(filename, 'wb') as file:
        file.write(image_data)

    print(f'图片已保存为 {filename}')
else:
    print('请求失败')
    print(response.status_code)
    print(response.text)

# 识别验证码
ocr = ddddocr.DdddOcr(beta=True)

with open("downloaded_image.jpg", 'rb') as f:
    image = f.read()

res = ocr.classification(image)
print(res)
