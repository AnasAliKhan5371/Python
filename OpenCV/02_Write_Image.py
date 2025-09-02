import cv2

img=cv2.imread("C:/Users/Anas Ali Khan/project/OpenCV/nature.jpg",0)

cv2.imshow("Natural Landscape",img)

cv2.imwrite('C:/Users/Anas Ali Khan/project/OpenCV/Nature Grey.jpg',img)

cv2.waitKey(0)

cv2.destroyAllWindows()