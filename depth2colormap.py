import cv2
import matplotlib.pyplot as plt

def depth2colormap(filename):
    image_GT=cv2.imread("./%s_GT.png"%filename,2) #读取灰度图像
    image_HR=cv2.imread("./%s_HR.png"%filename,2) #读取灰度图像
    image_LR=cv2.imread("./%s_LR.png"%filename,2) #读取灰度图像
    image1=cv2.applyColorMap(image_GT, cv2.COLORMAP_JET)
    image2=cv2.applyColorMap(image_HR, cv2.COLORMAP_JET)
    image3=cv2.applyColorMap(image_LR, cv2.COLORMAP_JET)
    cv2.imwrite("./%s_T_GT.png"%filename,image1) #保存热力图
    cv2.imwrite("./%s_T_HR.png"%filename,image2) #保存热力图
    cv2.imwrite("./%s_T_LR.png"%filename,image3) #保存热力图

depth2colormap(118)
depth2colormap(1406)