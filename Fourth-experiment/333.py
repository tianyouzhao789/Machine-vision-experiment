import cv2
import numpy as np
import matplotlib.pyplot as plt
#读取图像
img = cv2.imread('coin.jpg')
#使用分水岭算法分割此图片，显示处理过程中的效果图片
#转换为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
ishow = img.copy()
#不使用大律法二值化

#确定背景区域
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=3)
sure_bg = cv2.dilate(opening,kernel,iterations=3)
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret,sure_fg = cv2.threshold(dist_transform,0.1*dist_transform.max(),255,0)
sure_fg = np.uint8(sure_fg)
#未知区域
unknown = cv2.subtract(sure_bg,sure_fg)
ret,markers = cv2.connectedComponents(sure_fg)
markers = markers+1
markers[unknown==255] = 0
markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]
#显示二值图像
cv2.imshow('thresh',thresh)
#显示背景区域
cv2.imshow('sure_bg',sure_bg)
#显示前景区域
cv2.imshow('sure_fg',sure_fg)
#显示未知区域
cv2.imshow('unknown',unknown)
#显示分割结果
cv2.imshow('result',img)
cv2.waitKey()
cv2.destroyAllWindows()
