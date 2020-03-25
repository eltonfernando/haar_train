import cv2
import numpy as np

video='./fundo.avi'
cap = cv2.VideoCapture('./model_visualization.avi')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
out = cv2.VideoWriter('video_posd.avi', fourcc, 30, (width,height))
nome=0
while(True):
    re,frame=cap.read()
    #out.write(frame)
    nome+=1
    cv2.imwrite('./'+str(nome)+'.jpg',frame)

    print(nome)
    cv2.imshow('saida',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
#out.release()
cv2.destroyAllWindows()