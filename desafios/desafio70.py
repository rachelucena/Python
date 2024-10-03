print('_' * 30)
print('     LOJA SUPER BARATAO')
print('_' * 30)
total = 0
totmil = 0
quant = menor = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preco: R$'))
    total += preco
    quant += 1
    if preco > 1000:
        totmil += 1
    if quant == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
        print('------------ FIM DO PROGRAMA ------------')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato}, que custa {menor}')