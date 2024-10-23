jogador = dict()
jogador['nome'] = str(input(f'Nome do jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []

for c in range(jogador[f'partidas']):
    gols = int(input(f'Quantos gols na partida {c + 1}? '))
    jogador['gols'].append(gols)

jogador['total_gols'] = sum(jogador['gols'])

print('-=' * 30)
print(jogador)
print('-=' * 30)
print(f'O campo nome tem valor {jogador["nome"]}.')
print(f'O campo gols tem valor {jogador["gols"]}.')
print(f'O campo total tem valor {jogador["total_gols"]}.')
print('-=' * 30)
print((f'O jogador {jogador["nome"]} jogou {jogador['partidas']} partidas:'))
for i, gols in enumerate(jogador['gols']):
    print(f'    Na partida {i + 1}, fez {gols} gol(s).')
print(f'{jogador["nome"]} fez um total de {jogador['total_gols']} gols.')