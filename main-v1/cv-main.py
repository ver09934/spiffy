import cv2
import numpy as np
import math
import serialwriter

cap = cv2.VideoCapture(-1)

serialWriter = serialwriter.SerialWriter()

baseSpeed = 0.15
minSpeed = 0
maxSpeed = 1
kp = 0.12
ktest = 0.006

counter = 0

while True:

    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel_size = 5
    blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

    low_threshold = 50
    high_threshold = 150
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

    rho = 1  # distance resolution in pixels of the Hough grid
    theta = np.pi / 180  # angular resolution in radians of the Hough grid
    threshold = 15  # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 50  # minimum number of pixels making up a line
    max_line_gap = 20  # maximum gap in pixels between connectable line segments

    # Run Hough on edge detected image
    # Output "lines" is an array containing endpoints of detected line segments
    lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

    xVals = []
    angles = []

    if lines is not None:
        for line in lines:
            for x1,y1,x2,y2 in line:
                xVals.append((x1 + x2) / 2)
                angle = math.atan((y2 - y1) / (x2 - x1))
                angle = angle if angle > 0 else angle + np.pi
                angles.append(angle)

        averageX = sum(xVals) / len(xVals)
        xDev = averageX - (img.shape[1] / 2)
        avgAngle = sum(angles) / len(angles)
        angleDev = avgAngle - (np.pi / 2)
    else:
        xDev = 0
        angleDev = 0

    # angleDev += ktest * xDev

    leftSpeed = baseSpeed - kp * angleDev
    rightSpeed = baseSpeed + kp * angleDev

    leftSpeed = serialwriter.clamp(leftSpeed, 0, 1)
    rightSpeed = serialwriter.clamp(rightSpeed, 0, 1)

    serialWriter.setLeftPowerMapped(leftSpeed)
    serialWriter.setRightPowerMapped(rightSpeed)

    if counter % 4 == 0:
        serialWriter.writeAllBytes()
        print("--- SENT ---")
    counter += 1

    print(angleDev)

