import cv2

img=cv2.imread("C:/Users/Anas Ali Khan/project/OpenCV/nature.jpg",)

row=img.shape[1]
columns=img.shape[0]

centre=(columns/2,row/2)
angle=180

r=cv2.getRotationMatrix2D(centre,angle,1)

rotate=cv2.warpAffine(img,r,(columns,row)) #source,,dimensions

cv2.imshow("rotated",rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()