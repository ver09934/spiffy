import cv2
import numpy as np

# img = cv2.imread('../../../test.jpg')
img = cv2.imread('../../../1.jpg')

orig = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
ret, thresh = cv2.threshold(blurred, 30, 255, cv2.THRESH_BINARY_INV)

# img[400:,:] = [0, 0, 0]
# y_max = int(img.shape[0] * 0.95)
# thresh[y_max:,:] = 0
y_min = int(img.shape[0] * 0.8)
thresh[:y_min,:] = 0

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# _, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

if contours is not None and len(contours) > 0:
    main_contour = max(contours, key = cv2.contourArea)
    cv2.drawContours(img, [main_contour], -1, (0, 255, 0), 2)

    # rect = cv2.minAreaRect(main_contour)
    # box = cv2.boxPoints(rect)
    # box = np.int0(box)
    # cv2.drawContours(img, [box], -1, (0, 0, 255), 2)

    moments = cv2.moments(main_contour)
    center_x = int(moments["m10"] / moments["m00"])
    center_y = int(moments["m01"] / moments["m00"])
    cv2.circle(img, (center_x, center_y), 3, (0, 0, 255), 2) # last arg -1 solid

    img_centerline = img.shape[1] / 2
    x_deviation = center_x - img_centerline
    print(x_deviation)

else:
    pass # handle no contours found in thresholded image

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