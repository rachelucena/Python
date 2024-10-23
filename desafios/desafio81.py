valores =  []
while True:
    valor = int(input(f'Digite um valor: '))
    valores.append(valor)
    resp = str(input(f'Quer continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break

print(f'=-' * 30)
valores.sort(reverse=True)
print(f'Voce cadastrou {len(valores)} elementos')
print(f'Os valores em ordem decrescente sao {valores}')

if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista.')
