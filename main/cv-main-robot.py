import cv2
from cv2 import aruco
import numpy as np
import time
import serialwriter

serialWriter = serialwriter.SerialWriter()
time.sleep(3.5)

cap = cv2.VideoCapture(-1)
# out = cv2.VideoWriter('/home/pi/out.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (640, 480))

aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
parameters =  aruco.DetectorParameters_create()
# print(dir(parameters))
# parameters.polygonalApproxAccuracyRate = 0.1

# -- Original error --
# base_speed = 2
# kp = 0.01
# base_speed = 0.3
# kp = 0.001

# -- Squared error --
# base_speed = 0.3
# kp = 0.000005
base_speed = 0.25
kp = 0.000006

counter = 1
send_data_freq = 2
marker_freq = 5

x_deviation = 0

while True:

    start_time = time.time()

    # TODO: VERY IMPORTANT
    # If we pause for 10-15 seconds to perform an action, what will happen?
    # BAD: We start reading frames from the buffer where we left off...
    # GOOD: We start grabbing frames in real time
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

    # Square the error but maintain the sign
    tmp = x_deviation**2 * np.sign(x_deviation)

    if x_deviation > 0:
        leftSpeed = base_speed
        # rightSpeed = base_speed - (kp * x_deviation)
        rightSpeed = base_speed - (kp * tmp)
    else:
        # leftSpeed = base_speed + (kp * x_deviation)
        leftSpeed = base_speed + (kp * tmp)
        rightSpeed = base_speed

    leftSpeed = serialwriter.clamp(leftSpeed, 0, 1)
    rightSpeed = serialwriter.clamp(rightSpeed, 0, 1)

    serialWriter.setLeftPowerMapped(leftSpeed)
    serialWriter.setRightPowerMapped(rightSpeed)

    if counter % send_data_freq == 0:
        serialWriter.writeAllBytes()
        print("--- Sent Data ---")
    counter += 1

    marker_warning = ""

    # TODO: Only run when a marker is seen and then not seen
    if counter % marker_freq == 0:
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        # frame_markers = aruco.drawDetectedMarkers(img.copy(), corners, ids)

        if ids is not None:
            if len(ids) > 1:
                marker_warning = "WARNING: Multiple markers in frame"
            id = ids[0][0]
            if id == 39: # TODO: Move this hardcoded value to a variable

                serialWriter.setLeftPowerMapped(0)
                serialWriter.setRightPowerMapped(0)
                serialWriter.writeAllBytes()
                time.sleep(0.5)

                serialWriter.setStepperPositionMapped(0.25)
                serialWriter.writeAllBytes()
                time.sleep(6)

                serialWriter.setStepperPositionMapped(0)
                serialWriter.writeAllBytes()
                time.sleep(6)

    end_time = time.time()

    print("x-deviation: {:.0f} px\tlooptime: {:.4f} s\t{}".format(x_deviation, end_time - start_time, marker_warning))
