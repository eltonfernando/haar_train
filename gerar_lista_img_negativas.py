import os
local="./negativas"
lista=os.listdir(local)
with open('bg.txt','w') as file:
    for img in lista:
        file.write(local+'/'+img+'\n')