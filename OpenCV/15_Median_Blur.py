import cv2

img=cv2.imread("C:/Users/Anas Ali Khan/project/OpenCV/nature.jpg",)
resize=cv2.resize(img,(520,520))

# kernel size / only be +ve & odd
ksize=3
blur=cv2.medianBlur(resize,ksize)

cv2.imshow("Input",resize)
cv2.imshow("Output",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()