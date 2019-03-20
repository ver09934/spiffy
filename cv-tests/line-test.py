import cv2
import numpy as np
import math

def show(image):
    cv2.imshow('image', image)
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

img = cv2.imread('img.jpg')

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
line_image = np.copy(img) * 0  # creating a blank to draw lines on

# Run Hough on edge detected image
# Output "lines" is an array containing endpoints of detected line segments
lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

if lines is not None:
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),5)

xVals = []
angles = []

if lines is not None:
    for line in lines:
        for x1,y1,x2,y2 in line:
            xVals.append((x1 + x2) / 2)
            angle = math.atan((y2 - y1) / (x2 - x1))
            print(angle)
            angle = angle if angle > 0 else angle + np.pi
            angles.append(angle)

averageX = sum(xVals) / len(xVals)
xDev = (img.shape[1] / 2) - averageX
avgAngle = sum(angles) / len(angles)
angleDev = (np.pi / 2) - avgAngle

print("xDev: " + str(xDev))
print("angleDev: " + str(angleDev))

# Draw the lines on the  image
lines_edges = cv2.addWeighted(img, 0.8, line_image, 1, 0)

show(line_image)
