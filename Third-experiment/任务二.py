#encoding:utf-8
import cv2
import numpy as np

#读取图片
src = cv2.imread('aaa.png',cv2.IMREAD_UNCHANGED)
#设置卷积核
kernel = np.ones((5,5),np.uint8)
#图像开运算
result_open = cv2.morphologyEx(src,cv2.MORPH_OPEN,kernel)
#图像闭运算
result_close = cv2.morphologyEx(src,cv2.MORPH_CLOSE,kernel)
#图像梯度
result_grid = cv2.morphologyEx(src,cv2.MORPH_GRADIENT,kernel)
#图像顶帽
result_tophat = cv2.morphologyEx(src,cv2.MORPH_TOPHAT,kernel)
#图像黑帽
result_blackhat = cv2.morphologyEx(src,cv2.MORPH_BLACKHAT,kernel)
#显示图像
cv2.imshow("original",src)
cv2.imshow("result_open",result_open)
cv2.imshow("result_close",result_close)
cv2.imshow("result_grid",result_grid)
cv2.imshow("result_tophat",result_tophat)
cv2.imshow("result_blackhat",result_blackhat)
#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()