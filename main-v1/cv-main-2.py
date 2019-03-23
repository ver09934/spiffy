import cv2
import numpy as np
import math
'''
import serialwriter
import time

serialWriter = serialwriter.SerialWriter()
time.sleep(3.5)

cap = cv2.VideoCapture(-1)
while True:
ret, img = cap.read()
'''

img = cv2.imread('../../../test.jpg')

orig = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
ret, thresh = cv2.threshold(blurred, 30, 255, cv2.THRESH_BINARY_INV)

# 450, 250
y_max = int(img.shape[0] * 0.95)
y_min = int(img.shape[0] * 0.55)
thresh[y_max:,:] = 0
thresh[:y_min,:] = 0

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

if contours is not None and len(contours) > 0:

    main_contour = max(contours, key = cv2.contourArea)
    
    # TODO: Loop this until len(approx) == 4, changing decreasing arg #2 if <4 and increasing if >4
    # Admittedly not the best method, but then, none of this is...
    approx = cv2.approxPolyDP(main_contour, 20, True)

    cv2.drawContours(img, [main_contour], -1, (0, 255, 0), 2)
    cv2.drawContours(img, [approx], -1, (0, 0, 255), 2)

    x1 = (approx[1][0][0] + approx[2][0][0]) / 2
    y1 = (approx[1][0][1] + approx[2][0][1]) / 2

    x2 = (approx[0][0][0] + approx[3][0][0]) / 2
    y2 = (approx[0][0][1] + approx[3][0][1]) / 2

    avgX = (x1 + x2) / 2

    angle = math.atan((y2 - y1) / (x2 - x1))
    angle = angle if angle > 0 else angle + np.pi

    xDev = avgX - (img.shape[1] / 2)
    angleDev = angle - (np.pi / 2)

    print(angleDev * (180/np.pi))
    print(xDev)

    cv2.putText(img, 'Angle Deviation: ' + str(round(angleDev, 2)) + ' rad', (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(img, 'Shift: ' + str(xDev) + ' px', (5, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.imwrite('../../../tmp.jpg', img)

def showImg(img):
    cv2.imshow('img', img)
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# showImg(orig)
# showImg(thresh)
showImg(img)

