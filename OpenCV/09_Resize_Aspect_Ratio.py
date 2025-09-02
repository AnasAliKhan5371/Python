import cv2

img=cv2.imread("C:/Users/Anas Ali Khan/project/OpenCV/nature.jpg",)
print("Orignal Dimensions : ", img.shape)

scale=50
width=int(img.shape[1]*scale/100)
height=int(img.shape[1]*scale/100)
dim=(width,height)
resized=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
print("Resized Dimensions : ",resized.shape)

cv2.imshow("Orignal",img)
cv2.imshow("Resized",resized)

cv2.waitKey(0)
cv2.destroyAllWindows()