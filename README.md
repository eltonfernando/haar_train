# Trainando seu próprio cascade
Os arquivos cascade para detecção de faces olhos são bastante conhecidos, mais às vezes precisamos detectar outros objetos, se esse for o caso provavelmente tera que criar seu próprio arquivo. Nesse exemplo trainamos um cascade para detectar um óculo de sol. Você pode usar sua webcam para capturar dados necessários.

Vamos precisar de:
* Um vídeo (ou conjunto de imagens) que contém o objeto que você queira detectar.
* Um vídeo (ou conjunto de imagens) sem o objeto.
A partir desses vídeos vamos extrair os frames e criar nossas imagens positivas e negativas.
Nas pastas negativas e positivas estão as imagens que utilizei.

![Start](./gif/animation.gif)

## instalando pacotes
A biblioteca Opencv já possuem todas as ferramentas necessárias para treinar um cascade, isso facilita muito.

Se você estiver usando uma distribuição linux baseado no Debian é provável que isso funcione pra você.

``sudo apt install libopencv-dev``

## Construindo o projeto

Precisamos realizar algumas tarefas:
- (1) criar um arquivo bg.txt com o caminho para todas  as imagens negativas.
- (2) criar um arquivo info.txt contendo o caminho e as coordenado no objeto nas imagens positivas.
- (3) Criar um arquivo .vec a partir das imagens positivas.
 

`git clone https://github.com/eltonfernando/haar_train.git`

Entre na pasta haar_train, onde vamos trabalhar.

veja como criei o arquivo bg.txt usando o script [gerar_lista_img_negativas.py](gerar_lista_img_negativas.py)

O arquivo info.txt além do caminho temos que anotar as localização do objeto na imagem, para isso usamos a ferramenta opencv_annotation 


Para iniciar a ferramenta de anotação rode no terminal, passando o arquivo info.txt e a pasta com as imagens positivas:

`opencv_annotation -a=info.txt -i=positivas/`


obs: info.txt é o arquivo de anotação, ele deve estar em branco e a ferramenta não cria caso ele não exista

Com um clik você marca o ponto superior esquerdo do retângulo, arraste para desenhar e finaliza com segundo click. Após cada seleção, você tem as seguintes opções:

![start](./gif/annotation.gif)

* Pressionando c: confirme a anotação, (o retângulo deve ficar verde).

* Pressionar d: exclua a última anotação.

* Pressionando n: próxima imagem.

* Pressionando ESC: fecha janela

Com isso teremos o arquivo necessário para passar para o parâmetro -info de opencv_createsamples.

## Criando arquivo positives.vec

veja o script python [Prepara_train.py]()

Argumentos da linha de comando:

* `-vec positives.vec`: Nome do arquivo de saída que contém as amostras positivas para treinamento.

* `-bg bg.txt`: Uma lista com caminho das imagens negativas.

* `-num numPos`: Número de amostras positivas a serem geradas.

* `-w <Largura>`: Largura (em pixels) das amostras de saída.

* `-h <altura>`: Altura (em pixels) das amostras de saída.

Para executar o treinamento usaremos algumas variáveis definidas aqui, por isso coloquei tudo no mesmo arquivo [Prepara_train.py]()
