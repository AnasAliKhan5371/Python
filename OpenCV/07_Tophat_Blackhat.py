import cv2
import numpy as np


img=cv2.imread("C:/Users/Anas Ali Khan/project/OpenCV/nature.jpg")
width=600
height=850
dim=(width,height)
resized=cv2.resize(img,dim)

kernel=np.ones((5,5), dtype='uint8')

tophat=cv2.morphologyEx(resized,cv2.MORPH_TOPHAT,kernel)
blackhat=cv2.morphologyEx(resized,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow("Original",resized)
cv2.imshow("Top Hat",tophat)
cv2.imshow("Black Hat",blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()