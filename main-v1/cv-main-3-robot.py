import cv2
import numpy as np
import time
import serialwriter

serialWriter = serialwriter.SerialWriter()
time.sleep(3.5)

cap = cv2.VideoCapture(-1)
# out = cv2.VideoWriter('/home/pi/out.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (640, 480))

speed = 0.3

x_deviation = 0
gtzero_cur = False
gtzero_prev = False

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
        if moments["m00"] != 0:
            center_x = int(moments["m10"] / moments["m00"])
            # center_y = int(moments["m01"] / moments["m00"])

            # cv2.drawContours(img, [main_contour], -1, (0, 255, 0), 2)
            # cv2.circle(img, (center_x, center_y), 3, (0, 0, 255), 2) # last arg -1 solid

            img_centerline = img.shape[1] / 2
            x_deviation = center_x - img_centerline

    # out.write(img)
    print(x_deviation)


    gtzero_prev = gtzero_cur

    if x_deviation > 0:
        serialWriter.setLeftPowerMapped(speed)
        serialWriter.setRightPowerMapped(0)
        gtzero_cur = True
    else:
        serialWriter.setLeftPowerMapped(0)
        serialWriter.setRightPowerMapped(speed)
        gtzero_cur = False

    if gtzero_prev != gtzero_cur:
        serialWriter.writeAllBytes()
        print("--- Sent data ---")
