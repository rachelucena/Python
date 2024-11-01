import time
def contagem():
    print(f'-' * 30)
    print(f'Contagem de 1 a 10, de 1 em 1:')
    print(f'-' * 30)
    for c in range(1, 11):
        print(c, end=' ')
        time.sleep(1)
    print()

    print(f'-' * 30)
    print(f'Contagem de 10 a 0, de 2 em 2:')
    print(f'-' * 30)
    for c in range(10, -1, -2):
        print(c, end=' ')
        time.sleep(1)
    print()

    print()
    print(f'Agora e a sua vez de personalizar a contagem!')
    inicio = int(input(f'Inicio: '))
    fim = int(input(f'Fim: '))
    passo = int(input(f'Passo: '))
    print(f'-' * 30)
    print(f'Contagem de {inicio} a {fim}, de {passo} em {passo}')
    print(f'-' * 30)
    for c in range(inicio, fim + 1, passo):
        print(c, end=' ')
        time.sleep(1)
    print()

contagem()