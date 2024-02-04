#-- coding:utf-8 --
import cv2
import matplotlib.pyplot as plt
import numpy as np
#读取图像
img = cv2.imread(r'../Ice.jpg',0)
#r=0.5 , c = 1
img = np.double(img)
result1 = img**0.5
result1 = np.uint8(result1*255/np.max(result1))
#r=2 , c = 1
img = np.double(img)
result2 = img**2
result2 = np.uint8(result2*255/np.max(result2))
#显示图形
plt.figure(num='comparison')
titles = ['gray image','r=0.5','r=2']
images = [img, result1, result2]
for i in range(3):
    plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
