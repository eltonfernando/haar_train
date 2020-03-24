import os
def create_pos_n_neg():
    for file_type in ['neg']:

        for img in os.listdir(file_type):
            if file_type == 'pos':
                line = file_type + '/' + img + ' 1 0 0 20 20\n'
                with open('info.dat', 'a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type + '/' + img + '\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)
