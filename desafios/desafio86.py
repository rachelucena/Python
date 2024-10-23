matriz = [[0, 0, 0] for _ in range(3)]


for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite o valor para a posição [{i}][{j}]: '))


print('\nMatriz 3x3:')
for linha in matriz:
    print(linha)