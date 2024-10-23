valores = []
while True:
    n = int(input(f'Digite um valor: '))
    if n in valores:
        print(f'Valor duplicado, nao vou adicionar.')
    else:
        valores.append(n)
        print(f'Valor adicionado com sucesso!')
    resp = str(input(f'Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
valores.sort()
print(f'=-' * 30)
print(f'Voce digitou os valores {valores}')
