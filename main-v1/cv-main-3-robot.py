import cv2
import numpy as np
import time
import serialwriter

serialWriter = serialwriter.SerialWriter()
time.sleep(3.5)

cap = cv2.VideoCapture(-1)

baseSpeed = 0.3
kp = 0.05
counter = 1
countFreq = 2

while True:

    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    ret, thresh = cv2.threshold(blurred, 30, 255, cv2.THRESH_BINARY_INV)

    y_min = int(img.shape[0] * 0.8)
    thresh[:y_min,:] = 0

    _, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours is not None and len(contours) > 0:

        main_contour = max(contours, key = cv2.contourArea)

        moments = cv2.moments(main_contour)
        center_x = int(moments["m10"] / moments["m00"])

        img_centerline = img.shape[1] / 2
        x_deviation = center_x - img_centerline

    else:
        
        x_deviation = 0
    
    leftSpeed = baseSpeed - kp * angleDev
    rightSpeed = baseSpeed + kp * angleDev

    leftSpeed = serialwriter.clamp(leftSpeed, 0, 1)
    rightSpeed = serialwriter.clamp(rightSpeed, 0, 1)

    serialWriter.setLeftPowerMapped(leftSpeed)
    serialWriter.setRightPowerMapped(rightSpeed)

    if counter % countFreq == 0:
        serialWriter.writeAllBytes()
        print("--- Sent data ---")
    counter += 1
    
