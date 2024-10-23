import random
import time
dado = dict()
print('Valores sorteados:')
for c in range(1, 5):
    numero_sorteado = random.randint(1, 6)
    dado[f'Jogador {c}'] = numero_sorteado
    time.sleep(1)
    print(f'Jogador {c} tirou {numero_sorteado} no dado.')
print('-=' * 30)
print(f'=== RANKING DOS JOGADORES ===')
ranking = sorted(dado.items(), key=lambda x: x[1], reverse=True)
for pos, (jogador, valor) in enumerate(ranking, 1):
    time.sleep(1)
    print(f'{pos}º lugar: {jogador} com {valor}')