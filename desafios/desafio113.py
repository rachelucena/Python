def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um numero inteiro valido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuario!\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um numero inteiro valido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuario!\033[m')
            return 0
        else:
            return n


n1 = leiaint('Digite um numero inteiro: ')
print(f'O valor digitado foi {n1}')
n2 = leiaint('Digite um numero real: ')
print(f'O valor digitado foi {n2}')