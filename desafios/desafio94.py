pessoas = dict()
galera = list()
pessoas['total'] = []
soma = media = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))

    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print(f'Por favor, digite apenas M ou F.')

    pessoas['idade'] = int(input(f'Idade: '))
    soma += pessoas['idade']

    galera.append(pessoas.copy())

    while True:
        resp = str(input(f'Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print(f'Por favor, digite apenas S ou N.')

    if resp == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A media de idade e  {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'Ff':
        print(f'{p['nome']} ', end='')
print()
print(f'D) Lista das pessoas que estao acima da media: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('      ')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
