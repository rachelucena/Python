galera = list()
dados = list()
total = maior_peso = menor_peso = 0

while True:
    dados.append(str(input(f'Nome: ')))
    dados.append(float(input(f'Peso: ')))

    if total == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]

    galera.append(dados[:])
    dados.clear()
    total += 1
    resp = str(input(f'Quer continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break

maiores = []
menores = []

for pessoa in galera:
    if pessoa[1] == maior_peso:
        maiores.append(pessoa[0])
    if pessoa[1] == menor_peso:
        menores.append(pessoa[0])

print('=-' * 30)
print(f'Ao todo voce cadastrou {total} pessoas.')
print(f'O maior peso foi {maior_peso}Kg. Peso de {", ".join(maiores)}')
print(f'O menor peso foi {menor_peso}Kg. Peso de {", ".join(menores)}')
