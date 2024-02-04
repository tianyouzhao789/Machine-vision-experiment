#———————————————任务一—————————————————#
import cv2
#使用imread()函数读取图像，参数为图像的相对路径，并以numpy.ndarray的形式返回图像的像素矩阵
img = cv2.imread(r'i_building.jpg')
#查看图像的形状、大小、数据类型
print("Image shape: ", img.shape) #返回图像的形状，即（高度，宽度，通道数）
print("Image size: ", img.size)   #返回图像的像素数目
print("Image dtype: ", img.dtype) #返回图像的数据类型
#使用imshow()函数显示图像，参数为图像的窗口标题和图像的像素矩阵（即图像变量img）
cv2.imshow('image', img)
#使用waitKey()函数等待键盘输入，参数为等待时间（单位为毫秒），当参数为0时表示无限等待
#当参数为0时，按下任意键即可关闭图像窗口
cv2.waitKey(0)
#使用destroyAllWindows()函数关闭所有图像窗口
cv2.destroyAllWindows()
#———————————————任务二—————————————————#
#将图像从BGR空间转换为灰度图像
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image_gray', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
#将灰度图像转换为二值图像
#使用threshold()函数进行阈值分割，参数为图像的灰度矩阵、阈值、最大值、阈值类型
ret, img_binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('image_binary', img_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
#———————————————任务三\1—————————————————#
#对图像进行几何变换
#将图片高和宽分别赋值给x,y
x, y = img.shape[0:2]
#显示原图
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#缩放到原来的二分之一，输出尺寸格式为（宽，高）
img_test1 = cv2.resize(img, (int(y/2), int(x/2)))
cv2.imshow('image_test1', img_test1)
cv2.waitKey(0)
cv2.destroyAllWindows()
#最近领域插值法缩放
#缩放到原来的四分之一
img_test2 = cv2.resize(img, (int(y/4), int(x/4)), interpolation=cv2.INTER_NEAREST)
cv2.imshow('image_test2', img_test2)
cv2.waitKey(0)
cv2.destroyAllWindows()
#放大到原来的两倍
img_test3 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
cv2.imshow('image_test3', img_test3)
cv2.waitKey(0)
cv2.destroyAllWindows()
#———————————————任务三\2—————————————————#
#图像的旋转
#获取图像的高和宽
height, width = img.shape[0:2]
# 获取图像绕着图像中心点的旋转矩阵
matRotate = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)
#进行仿射变换
img_test4 = cv2.warpAffine(img, matRotate, (width, height))
cv2.imshow('image_test4', img_test4)
cv2.waitKey(0)
cv2.destroyAllWindows()
#———————————————任务三\3—————————————————#
#图像的翻转
h_flip = cv2.flip(img, 1) #水平翻转
cv2.imshow('image_h_flip', h_flip)
cv2.waitKey(0)
cv2.destroyAllWindows()
v_flip = cv2.flip(img, 0) #垂直翻转
cv2.imshow('image_v_flip', v_flip)
cv2.waitKey(0)
cv2.destroyAllWindows()
hv_flip = cv2.flip(img, -1) #水平垂直翻转
cv2.imshow('image_hv_flip', hv_flip)
cv2.waitKey(0)
cv2.destroyAllWindows()
#———————————————任务四—————————————————#
#对图像进行保存
#使用imwrite()函数保存图像，参数为图像的保存路径和图像的像素矩阵
retval1 = cv2.imwrite('i_building_gray.jpg', img_gray)
retval2 = cv2.imwrite('i_building_binary.jpg', img_binary)
retval3 = cv2.imwrite('i_building_test1.jpg', img_test1)
retval4 = cv2.imwrite('i_building_test2.jpg', img_test2)
retval5 = cv2.imwrite('i_building_test3.jpg', img_test3)
retval6 = cv2.imwrite('i_building_test4.jpg', img_test4)
retval7 = cv2.imwrite('i_building_h_flip.jpg', h_flip)
retval8 = cv2.imwrite('i_building_v_flip.jpg', v_flip)
retval9 = cv2.imwrite('i_building_hv_flip.jpg', hv_flip)
#查看保存结果
print("retval1: ", retval1)
print("retval2: ", retval2)
print("retval3: ", retval3)
print("retval4: ", retval4)
print("retval5: ", retval5)
print("retval6: ", retval6)
print("retval7: ", retval7)
print("retval8: ", retval8)
print("retval9: ", retval9)