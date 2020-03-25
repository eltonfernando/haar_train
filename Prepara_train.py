import os

w=80
h=42
numPos=len(os.listdir('./positivas'))
numNeg=len(os.listdir("./negativas"))
numStages=6

createsamples="opencv_createsamples "
createsamples+='-bg bg.tx '
createsamples+='-info info.txt '
createsamples+='-num '+str(numPos)+' '
createsamples+='-w '+str(w)+' '
createsamples+='-h '+str(h)+' '
createsamples+='-vec positives.vec'


#print(createsamples)
os.system(createsamples)

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
os.system(train)
print(train)

cmd_result='opencv_visualisation --image=./modelo.png --model=./data/cascade.xml --data=data/log/'
os.system(cmd_result)
