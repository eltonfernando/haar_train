import os

w=60
h=30

total_amostra_criada=len(os.listdir('./data/testimages'))
num_img_vec=total_amostra_criada

numNeg=500
numPos=total_amostra_criada
numStages=30

cmd_amostra='opencv_createsamples -bg bg.txt' \
                                ' -info info.txt' \
                                ' -pngoutput saida ' \
                                '-maxxangle 0.5 ' \
                                '-maxyangle 0.5 ' \
                                '-maxzangle 0.5' \
                                ' -num '+str(total_amostra_criada)+' '\
                                '-w '+str(w)+' '\
                                '-h '+str(h)+' '\
                                '-vec positives.vec '\
                                '-show True'

print(cmd_amostra)
os.system(cmd_amostra)

cmd_train='opencv_traincascade ' \
          '-data data ' \
          '-vec positives.vec ' \
          '-bg bg.txt ' \
          '-numPos '+str(numPos)+' ' \
          '-numNeg '+str(numNeg)+' ' \
          '-numStages '+str(numStages)+' ' \
          '-w '+str(w)+' ' \
          '-h '+str(h)+' -numThreads 4'
#os.system(cmd_train)

cmd_result='opencv_visualisation --image=./36.jpg --model=./data/cascade.xml --data=data/log/'

#os.system(cmd_result)
