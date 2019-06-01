import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

# pip install pillow opencv-python matplotlib pandas aruco

import time

cap = cv2.VideoCapture(2)

while(True):

    start_time = time.time()
    
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    parameters =  aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)

    cv2.imshow('img', frame_markers)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # print("looptime: {} s" .format(time.time() - start_time))

    if ids is not None:
        for id in ids:
            print(id[0], end=' ')
        print()

cap.release()
cv2.destroyAllWindows()
