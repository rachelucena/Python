jogador = dict()
partidas = list()
time = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input(f'Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input(f'Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print(f'Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Nao existe jogador com codigo {busca}.')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
#print('-=' * 30)
#print(jogador)
#print('-=' * 30)
#for k, v in jogador.items():
#    print(f'O campo {k} tem valor {v}.')
#print('-=' * 30)
#print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
#for i, v in enumerate(jogador['gols']):
#    print(f'    => Na partida {i} fez {v} gols.')
#print(f'Foi um total de {jogador["total"]} gols.')