#canny edge detection(algos.)
#1 noise reduction
#2 Intensity of gradient
#3 non-max supression
#4 thresholding
import cv2
import numpy as np

img=cv2.imread("C:/Users/Anas Ali Khan/project/OpenCV/nature.jpg",0)
resize=cv2.resize(img,(520,520))
min_thresh=100 #below 100-black
max_thresh=200 #above 200-white
edges=cv2.Canny(resize,min_thresh,max_thresh)

cv2.imshow("Input",resize)
cv2.imshow("Output",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()