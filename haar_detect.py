import numpy as np
import cv2


# this is the cascade we just made. Call what you want
watch_cascade = cv2.CascadeClassifier('./data/cascade.xml')

cap = cv2.VideoCapture('./output4.avi')

while 1:
    ret, img = cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #gray=cv2.resize(gray,(100,100))
    # add this
    # image, reject levels level weights.
    watches = watch_cascade.detectMultiScale(gray,scaleFactor=1.2,
    minNeighbors=1,
    minSize=(18, 18),maxSize=(21,21))

    # add this
    for (x, y, w, h) in watches:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()