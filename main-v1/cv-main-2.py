import cv2
import numpy as np
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

y_max = int(img.shape[0] * 0.625)
thresh[:y_max,:] = 0 # img[400:,:] = [0, 0, 0]

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

if contours is not None and len(contours) > 0:
    main_contour = max(contours, key = cv2.contourArea)
    cv2.drawContours(img, [main_contour], -1, (0, 255, 0), 2)
    rect = cv2.minAreaRect(main_contour)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(img, [box], -1, (0, 0, 255), 2)

def showImg(img):
    cv2.imshow('img', img)
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

showImg(orig)
showImg(thresh)
showImg(img)


def main():
    pass

if __name__ == "__main__":
    main()