print('=================== LOJAS GUANABARA ==================')
preco = float(input('Preco das compras: '))
print('FORMAS DE PAGAMENTO:')
print('[ 1 ] Valor a vista')
print('[ 2 ] a vista cartao')
print('[ 3 ] 2x no cartao')
print('[ 4 ] 3x ou mais no cartao')
opcao = int(input('Qual e a opcao? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('Pagando a vista, a compra sai de R${:.2f} por R${:.2f}'.format(preco, total))
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('Pagando a vista no cartao, a compra sai de R${:.2f} por R${:.2f}'.format(preco, total))
elif opcao == 3:
    total = preco
print('Pagando em ate duas vezes no cartao, a compra sai por R${:.2f}'.format(total))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    print('Pagando parcelado a partir de tres vezes, a compra sai de R${:.2f} por R${:.2f}'.format(preco, total))
else:
    print('Digite uma opcao valida.')