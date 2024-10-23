print('_' * 30)
print('      Jogo da Mega Sena')
print('_' * 30)

import random

quant_jogos = int(input(f'Quantos jogos da Mega Sena voce quer jogar? '))
tds_jogos = []

for c in range(quant_jogos):
    jogo = []
    while(len(jogo)) < 6:
        n = random.randint(1, 60)
        if n not in jogo:
            jogo.append(n)
    jogo.sort()
    tds_jogos.append(jogo)

for i, jogo in enumerate(tds_jogos, 1):
    print(f'Jogo {i}: {jogo}')