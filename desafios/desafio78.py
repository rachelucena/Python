pos0 = int(input(f'Digite um numero para a posicao 0: '))
pos1 = int(input(f'Digite um numero para a posicao 1: '))
pos2 = int(input(f'Digite um numero para a posicao 2: '))
pos3 = int(input(f'Digite um numero para a posicao 3: '))
pos4 = int(input(f'Digite um numero para a posicao 4: '))
print(f'=-' * 30)
numeros = [pos0, pos1, pos2, pos3, pos4]
print(f'Voce digitou os valores {numeros}')
maior_valor = max(numeros)
menor_valor = min(numeros)
posicoes_maior = [i for i, v in enumerate(numeros) if v == maior_valor]
posicoes_menor = [i for i, v in enumerate(numeros) if v == menor_valor]
print(f'O maior valor digitado foi {max(numeros)} na(s) posicao(oes) {posicoes_maior}')
print(f'O menor valor digitado foi {min(numeros)} na(s) posicao(oes) {posicoes_menor}')

# print(f'O maior valor sorteado foi {max(numeros)}')
# print(f'O menor valor sorteado foi {min(numeros)}')
# print(f'O valor 3 apareceu na {numeros.index(3)+1} posicao.')
# for c in range(0, 5):
    # listanum.append(int(input(f'Digite um valor para a posicao {c}: ')))