import cv2

cap = cv2.VideoCapture(-1)

while True:
    
    ret, img = cap.read()
    cv2.imwrite("test.jpg", img)

    '''
    import time
    time.sleep(1)
    '''

# sudo python -m SimpleHTTPServer 80
