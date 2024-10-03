tot18 = homem = mulher = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'O total de pessoas com mais de 18 anos e {tot18}. Ao todos temos {homem} homens cadastrados. E temos {mulher} mulheres menores de 20 anos.')

