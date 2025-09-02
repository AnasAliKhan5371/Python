import cv2

img=cv2.imread("C:/Users/Anas Ali Khan/project/OpenCV/nature.jpg",)
width=600
height=850
dim=(width,height)
resized=cv2.resize(img,dim)
print("size in bytes: ",img.size)

cv2.imshow("Orignal",resized)

# HORIZONTAL FLIP
flip=cv2.flip(resized,1)
cv2.imshow("Horizontal",flip)

# VERTICAL FLIP
flip_1=cv2.flip(resized,0)
cv2.imshow("Vertical",flip_1)

# HORIZONTAL & VERTICAL FLIP
flip_2=cv2.flip(resized,-1)
cv2.imshow("Horizontal & Vertical",flip_2)

cv2.waitKey(0)
cv2.destroyAllWindows()