import cv2
import numpy as np

#img=cv2.imread("C:/Users/Anas Ali Khan/project/OpenCV/nature.jpg",cv2.IMREAD_COLOR)
img=np.zeros(shape=[600,800,3],dtype='uint8')
cv2.line(img,(0,0),(150,150),(255,0,0),2 ) #((point 1),(point 2),(color),thickness)
cv2.rectangle(img,(200,150),(250,300),(0,255,0),3)#top left,bottom right
cv2.circle(img,(300,75),70,(255,0,255),3) # centre, radius

pts_polygon=np.array([[100,50],[100,300],[500,50],[500,300]],np.int32)
cv2.polylines(img,[pts_polygon],True,(0,255,255),3)# points,

font=cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img,'HELLO !',(10,500),font,3,(200,255,255),8,cv2.LINE_AA) # 'HELLO !', Bottom left corner coordinate,font,font scale,color,thick,proper space

cv2.imshow("IMAGE",img)
cv2.waitKey(0)
cv2.destroyAllWindows()