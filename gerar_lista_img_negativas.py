#pyhton

from os.path import join
from glob import glob
def generate_file_negative(path_img_negative,out):
    lista_img=glob(path_img_negative)
    print(len(lista_img))
    if len(lista_img)==0:
        print("path",path_img_negative)
        raise Exception("não encontrou imagens")
    with open(out,"w") as file:
        for path_img in lista_img:
            file.write(f'{path_img}\n')

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='dir img nevative',required=True)
    parser.add_argument("--out",default="bg.txt",help="dir file txt anotation")
    args = parser.parse_args()
    print(args.input)
    generate_file_negative(join(args.input,"*.jpg"),args.out)
