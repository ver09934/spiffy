import cv2

cap = cv2.VideoCapture(-1)

ret, img = cap.read()
cv2.imwrite("~/test.jpg", img)

# sudo python -m SimpleHTTPServer 80

