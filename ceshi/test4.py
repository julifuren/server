import cv2

# # 读照片
# img = cv2.imread('1.jpg')
# # 读取像素点
# pixel=img[413,519]
# print('img[413,519]:',pixel)
# pixel=img[413,520]
# print('img[161,199]:',pixel)


img = cv2.imread('2.jpg')
pixel = str(img[413, 519])
print('img[413,519]:', pixel)
if pixel == '[139 216 248]':
    print('正确')
