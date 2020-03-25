
import cv2
import os
watch_cascade = cv2.CascadeClassifier('./cascade/oculos.xml')

list_img=os.listdir('./img_teste')

for img_name in list_img:
    img = cv2.imread('./img_teste/'+img_name)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    watches = watch_cascade.detectMultiScale(gray,scaleFactor=1.2,
    minNeighbors=1,
    minSize=(30, 20),maxSize=(90,60))

    # add this
    for (x, y, w, h) in watches:
        cv2.rectangle(img, (x - 4, y + h), (x + w + 5, y + h + 16), (255, 0, 0), cv2.FILLED)
        cv2.putText(img, 'Oculos de sol', (x - 4, y + h + 13), cv2.FONT_ITALIC, 0.42, (255, 255, 255), 1)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('img', img)
    #cv2.imwrite(img_name+'.png',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()