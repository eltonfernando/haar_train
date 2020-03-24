import cv2
import numpy as np
camera_loja='rtsp://admin:Ti224466@velmondssa.dyndns.org:559/ch1/sub/av_stream'
video='./fundo.avi'
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
out = cv2.VideoWriter('video_negativo.avi', fourcc, 30, (width,height))
nome=595
while(True):
    re,frame=cap.read()
    out.write(frame)
    cv2.imwrite('./img_negativo/'+str(nome)+'.jpg',frame)
    nome+=1
    print(nome)
    cv2.imshow('saida',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
#out.release()
cv2.destroyAllWindows()