import cv2
import os
import matplotlib.pyplot as plt
def resize_neg():
    for imagem in os.listdir('./original_neg'):
        print(imagem)
        img=cv2.imread('./original_neg/'+imagem)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        nova=cv2.resize(img,(100,100))
        cv2.imwrite('./neg/'+str(imagem),nova)
def resize_pos():
    img=cv2.imread('./515.jpg')
    img=img[150:170, 168:188]
    print(img.shape)
    plt.imshow(img)
    plt.show()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #gray=cv2.resize(gray,(50,50))
    cv2.imshow('resize_pos',gray)
    cv2.waitKey(0)
    cv2.imwrite('./women.jpg',gray)
    cv2.destroyAllWindows()
#resize_pos()