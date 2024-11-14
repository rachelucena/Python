import contas

num = float(input('Digite o preco: R$'))
print(f'A metade do preco R${num:.2f} e R${contas.metade(num):.2f}')
print(f'O dobro do preco R${num:.2f} e R${contas.dobro(num):.2f}')
print(f'Aumentando 10% temos R${contas.porc(num)}')
