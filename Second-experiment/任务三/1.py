#-*- coding:utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
#读取图片
img = cv2.imread('../Ice.jpg')
#灰度转换
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#局部直方图均衡化处理
clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(10,10))
#将灰度图像和局部直方图相关联，把直方图均衡化应用于灰度图
result = clahe.apply(gray)
#显示图像
plt.subplot(221)
plt.imshow(gray,cmap=plt.cm.gray),plt.axis('off'),plt.title('(a)')
plt.subplot(222)
plt.imshow(result,cmap=plt.cm.gray),plt.axis('off'),plt.title('(b)')
plt.subplot(223)
plt.hist(gray.ravel(),256),plt.title('(c)')
plt.subplot(224)
plt.hist(result.ravel(),256),plt.title('(d)')
plt.show()

