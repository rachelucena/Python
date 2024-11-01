from time import sleep

c = ('\033[m', # sem cor
     '\033[0;30;41m', # vermelho
     '\033[92m', # verde
     '\033[93m', # amarelo
     '\033[94m', # azul
     '\033[95m', # roxo
     '\033[97m' # branco
     );

def ajuda(com):
    titulo(f'Acessando o manual do comando \{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')
    sleep(1)


# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 1)
    comando = str(input("Funcao ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO!', 1)