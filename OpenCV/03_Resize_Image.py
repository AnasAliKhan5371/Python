import cv2

img=cv2.imread("C:/Users/Anas Ali Khan/project/OpenCV/nature.jpg")

print("Dimensions of image:",img.shape)
width=img.shape[1]  #unchanged
height=200           #image.shape[0]
dim=(width,height)
resized=cv2.resize(img,dim)

cv2.imshow("Natural Landscape",resized)

cv2.waitKey(0)

cv2.destroyAllWindows()