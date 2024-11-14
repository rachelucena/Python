import contas

num = float(input('Digite o preco: R$'))
print(f'A metade do preco {num} e {contas.metade(num)}')
print(f'O dobro do preco {num} e {contas.dobro(num)}')
print(f'Aumentando 10% temos {contas.porc(num)}')