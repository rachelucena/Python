import contas

num = float(input('Digite o preco: R$'))
print(f'A metade do preco {contas.formatar_moeda(num)} e {contas.formatar_moeda(contas.metade(num))}')
print(f'O dobro do preco {contas.formatar_moeda(num)} e {contas.formatar_moeda(contas.dobro(num))}')
print(f'Aumentando 10% temos {contas.formatar_moeda(contas.porc(num))}')