import cv2
from cv2 import aruco
import numpy as np
import time
import serialwriter

serialWriter = serialwriter.SerialWriter()
time.sleep(3.5)

cap = cv2.VideoCapture(-1)
# out = cv2.VideoWriter('/home/pi/out.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (640, 480))
# TODO: Fancy image for poster

aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
parameters =  aruco.DetectorParameters_create()
# print(dir(parameters))
# parameters.polygonalApproxAccuracyRate = 0.3
# parameters.errorCorrectionRate = 1

# ------------------
# base_speed = 0.25
# kp = 0.001
# ki = 0.0
# ------------------
# base_speed = 0.25
# kp = 0.0006
# ki = 0.0
# ------------------
base_speed = 0.25
kp = 0.0005
ki = 0.00006
# ------------------

counter = 1
send_data_freq = 2
marker_freq = 5

x_deviation = 0
i_term = 0
looptime = 0
start_time = time.time()

zero_iterm = False

prev_id = None

while True:

    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    # ret, thresh = cv2.threshold(blurred, 70, 255, cv2.THRESH_BINARY_INV)
    ret, thresh = cv2.threshold(blurred, 180, 255, cv2.THRESH_BINARY)

    y_min = int(img.shape[0] * 0.35)
    thresh[:y_min,:] = 0

    # TODO: Remove if looptime too long
    # kernel = np.ones((5,5),np.uint8)
    # thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

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

    end_time = time.time()
    looptime = end_time - start_time
    start_time = time.time()

    p_term = kp * x_deviation
    i_term += ki * x_deviation * looptime
    if zero_iterm == True:
        i_term = 0
        zero_iterm = False
    output = p_term + i_term

    if x_deviation > 0:
        leftSpeed = base_speed
        rightSpeed = base_speed - output
    else:
        leftSpeed = base_speed + output
        rightSpeed = base_speed

    leftSpeed = serialwriter.clamp(leftSpeed, 0, 1)
    rightSpeed = serialwriter.clamp(rightSpeed, 0, 1)

    serialWriter.setLeftPowerMapped(leftSpeed)
    serialWriter.setRightPowerMapped(rightSpeed)

    if counter % send_data_freq == 0:
        serialWriter.writeAllBytes()
        print("--- Sent Data ---")
    counter += 1

    # TODO: Only run when a marker is seen one iteration and then not seen the next iteration
    # TODO: Don't detect two of the same marker consecutively
    if counter % marker_freq == 0:
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        # frame_markers = aruco.drawDetectedMarkers(img.copy(), corners, ids)

        if ids is not None:

            zero_iterm = True # Otherwise the i-term grows very large, since this interruption makes the looptime very long
            
            id = ids[0][0]
            
            if (id == 38 and prev_id != 38) or (id == 39 and prev_id != 39):

                serialWriter.setLeftPowerMapped(0)
                serialWriter.setRightPowerMapped(0)
                serialWriter.writeAllBytes()
                time.sleep(0.5)

                serialWriter.setStepperPositionMapped(1)
                serialWriter.writeAllBytes()
                time.sleep(24)

                serialWriter.setBit(2, 1)
                serialWriter.writeAllBytes()
                time.sleep(5)
                serialWriter.setBit(2, 0)
                serialWriter.writeAllBytes()
                time.sleep(0.5)

                '''
                serialWriter.setBit(1, 1)
                serialWriter.writeAllBytes()
                time.sleep(2)
                serialWriter.setBit(1, 0)
                serialWriter.writeAllBytes()
                time.sleep(0.5)
                '''

                serialWriter.setStepperPositionMapped(0)
                serialWriter.writeAllBytes()
                time.sleep(24)

            if id == 40:

                serialWriter.setLeftPowerMapped(0)
                serialWriter.setRightPowerMapped(0)
                serialWriter.writeAllBytes()
                break

            prev_id = id

    # TODO: Need more telem for PI controller
    print("x-deviation: {:.0f} px\tlooptime: {:.4f} s".format(x_deviation, looptime))

cap.release()
