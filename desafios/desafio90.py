situacao = dict()
situacao['nome'] = str(input(f'Nome: '))
situacao['media'] = float(input(f'Media de {situacao["nome"]}: '))
print('-=' * 20)
print(f'O nome e {situacao["nome"]}')
print(f'A media e {situacao["media"]}')
if situacao['media'] <= 5:
    print('Situacao e igual a REPROVADO')
elif 5 <= situacao['media'] < 7:
    print('Situacao e igual a RECUPERACAO')
else:
    print('Situacao e igual a APROVADO')