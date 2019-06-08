import cv2

cap = cv2.VideoCapture(-1)

for i in range(0, 100):
    ret, img = cap.read()

cv2.imwrite("/home/pi/test.jpg", img)

# sudo python -m SimpleHTTPServer 80

