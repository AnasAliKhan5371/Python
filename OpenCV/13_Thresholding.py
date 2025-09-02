# exceed threshold value- white
# below threshold value- same

import cv2
import numpy as np

img=cv2.imread("C:/Users/Anas Ali Khan/project/OpenCV/nature.jpg",)

threshold_value=100

_,binary_threshold=cv2.threshold(img,threshold_value,255,cv2.THRESH_BINARY)

cv2.imshow("Orignal",img)
cv2.imshow("binary Threshold", binary_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()