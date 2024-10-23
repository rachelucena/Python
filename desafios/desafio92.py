from datetime import datetime
info = dict()
info['nome'] = str(input(f'Nome: '))
info['ano'] = int(input(f'Ano de nascimento: '))

ano_atual = datetime.now().year
idade = ano_atual - info['ano']

info['carteira'] = int(input(f'Carteira de trabalho (0 nao tem): '))

if info['carteira'] != 0:
    info['contratacao'] = int(input(f'Ano de contratacao: '))
    info['salario'] = float(input(f'Salario: R$ '))

    info['aposentadoria'] = idade + ((info['contratacao'] + 35) - ano_atual)

print('-=' * 30)
print(f'O nome e {info["nome"]}')
print(f'A idade e {idade}')
print(f'CPTS e {info["carteira"]}')

if info['carteira'] != 0:
    print((f'O salario e {info["salario"]:.2f}'))
    print(f'A aposentadoria de {info["nome"]} sera aos {info["aposentadoria"]} anos')
