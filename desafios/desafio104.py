def leiaInt():
    while True:
        try:
            n = int(input('Digite um numero: '))
            return n
        except ValueError:
            print('\033[91mEntrada invalida! Por favor, digite um numero inteiro.\033[0m')

n = leiaInt()
print(f'Voce digitou o numero {n}')