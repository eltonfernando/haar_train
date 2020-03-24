#criando positivo
sudo apt install libopencv-dev

opencv_createsamples -img men.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1500

opencv_createsamples -info info/info.lst -num 800 -w 50 -h 50 -vec positives.vec


opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 800 -numNeg 400 -numStages 10 -w 40 -h 40

opencv_visualisation --image=men.jpg --model=data/cascade.xml --data=./

