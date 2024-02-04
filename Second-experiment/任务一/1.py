#——————————任务一————————————#
import cv2
import matplotlib.pyplot as plt
import numpy as np
#读取图像
img = cv2.imread(r'../Ice.jpg', 0)
#获取图像的高度和宽度
height = img.shape[0]
width = img.shape[1]
#创建一幅图像，uint8是专门用于存储各种图像的（包括RGB，灰度图像等），范围是0-255
reasult = np.zeros((height,width), np.uint8)
reasult1 = np.zeros((height,width), np.uint8)
#图像灰度反转
#---------------------方法一-----------------------#
reasult[:,:] = 255-img[:,:]
#---------------------方法二-----------------------#
# for i in range(height):
#     for j in range(width):
#         gray = -(img[i,j])+255
#         reasult[i,j] = gray
#图像灰度上移
for i in range(height):
    for j in range(width):
        if(img[i,j])+50>255:
            gray = 255
        else:
            gray = (img[i,j])+50
        reasult1[i,j] = np.uint8(gray)
#显示图形
plt.figure(num='comparison')
titles = ['gray image','gray scale inversion','brightness increased']
images = [img, reasult, reasult1]
for i in range(3):
    plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

