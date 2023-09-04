import cv2

# 0 because not multiple webcam, just 1 camera
cam = cv2.VideoCapture(0)

# turn on camera
while cam.isOpened():

    #read the camera
    ret, frame1 = cam.read()

    #create another frame (for comparing)
    ret, frame2 = cam.read()

    # detect differences (motions)
    diff = cv2.absdiff(frame1, frame2)

    # turn it into gray
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)

    # blur it
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # create threshold
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    
    # dilation
    dilated = cv2.dilate(thresh, None, iterations=3)

    # boundary or the border
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # draw that contour on your screen
    cv2.drawContours(frame1, contours, -1, (0.255, 0), 2)
    
    # # detect the big part
    # for c in contours:
    #     if cv2.contourArea(c)

    # how to close the popup
    if cv2.waitKey(10) == ord('q'):
        break
    
    #show that in the computer
    cv2.imshow('Security Camera', frame1)