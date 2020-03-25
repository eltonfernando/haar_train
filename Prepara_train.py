import os
import pandas as pd
df=pd.read_csv('info.txt',delimiter=' ')

w=int(df['82'].mean())
h=int(df['28'].mean())
numPos=len(os.listdir('./positivas'))
numNeg=len(os.listdir("./negativas"))
numStages=15

createsamples="opencv_createsamples "
createsamples+='-bg bg.tx '
createsamples+='-info info.txt '
createsamples+='-num '+str(numPos)+' '
createsamples+='-w '+str(w)+' '
createsamples+='-h '+str(h)+' '
createsamples+='-vec positives.vec'

#print(createsamples)
#os.system(createsamples)

train='opencv_traincascade '
train+='-data data '
train+='-vec positives.vec '
train+='-bg bg.txt '
train+='-numPos '+str(numPos)+' '
train+='-numNeg '+str(numNeg)+' '
train+='-numStages '+str(numStages)+' '
train+='-w '+str(w)+' '
train+='-h '+str(h)+' '
train+= '-precalcValBufSize 2024 '
train+= '-precalcIdxBufSize 2024'
#os.system(train)
print(train)

cmd_result='opencv_visualisation --image=./modelo.png --model=./cascade/oculos.xml --data=data/log/'
os.system(cmd_result)
