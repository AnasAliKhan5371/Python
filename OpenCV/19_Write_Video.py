import cv2

video=cv2.VideoCapture("C:/Users/Anas Ali Khan/project/OpenCV/river.mp4")

fourcc=cv2.VideoWriter_fourcc(*'mp4v')  # compress code
output=cv2.VideoWriter('Output.mp4',fourcc,30,(1280,720))

while video.isOpened():
    ret,frame=video.read()
    if ret:
        output.write(frame)
        cv2.imshow('frame',frame)

        if cv2.waitKey(10)==ord('s'):
            break
    else:
        break

cv2.destroyAllWindows()