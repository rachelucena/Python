matriz = [[0, 0, 0] for _ in range(3)]


for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite o valor para a posição [{i}][{j}]: '))


soma_pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = matriz[1][0]


for i in range(3):
    for j in range(3):

        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]


        if j == 2:
            soma_terceira_coluna += matriz[i][j]


        if i == 1 and matriz[i][j] > maior_segunda_linha:
            maior_segunda_linha = matriz[i][j]


print('\nMatriz 3x3:')
for linha in matriz:
    print(linha)


print(f'\nSoma dos valores pares: {soma_pares}')
print(f'Soma dos valores da terceira coluna: {soma_terceira_coluna}')
print(f'Maior valor da segunda linha: {maior_segunda_linha}')