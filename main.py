import cv2
# 0 because not multiple webcam
cam = cv2.VideoCapture(0)

# turn on camera
while cam.isOpened():
    #read the camera
    ret, frame = cam.read()

    # how to close the popup
    if cv2.waitKey(10) == ord('q'):
        break
    
    #show that in the computer
    cv2.imshow('Security Camera', frame)