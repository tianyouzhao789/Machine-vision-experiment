#encoding:utf-8
import cv2
import numpy as np
#读取图片
src1 = cv2.imread('test01.jpg',-1)
src2 = cv2.imread('test02.png',-1)
#设置卷积核
kernel = np.ones((5,5),np.uint8)
#图像腐蚀
erosion1 = cv2.erode(src1,kernel)
#图像膨胀
dilation1 = cv2.dilate(src1,kernel)
#显示图像
cv2.imshow('e-src',src1)
cv2.imshow('erosion',erosion1)
cv2.imshow('d-src',src2)
cv2.imshow('dilation',dilation1)
#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()