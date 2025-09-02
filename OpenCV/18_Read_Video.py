import cv2

video=cv2.VideoCapture("C:/Users/Anas Ali Khan/project/OpenCV/river.mp4")

while video.isOpened():
    _,frame=video.read()
    frame=cv2.resize(frame,(800,720))

    cv2.imshow("output",frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cv2.destroyAllWindows()