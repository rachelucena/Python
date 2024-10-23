lista = []
pares = []
impares = []
par = impar = 0
while True:
    valor = int(input(f'Digite um valor: '))
    lista.append(valor)
    resp = str(input(f'Quer continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break

    if valor % 2 == 0:
        par += 1
        pares.append(valor)
    if valor % 2 != 0:
        impar += 1
        impares.append(valor)

print(f'=-' * 30)
print(f'A lista completa e {lista}')
print(f'A lista de pares e {pares}')
print(f'A lista de impares e {impares}')