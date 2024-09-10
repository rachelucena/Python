tab = int(input('Digite um numero para ver sua tabuada: '))
print('TABUADA DO NUMERO {}'.format(tab))
for c in range(1, 11):
    resultado = tab * c
    print('{} X {} = {}'.format(tab, c, resultado))