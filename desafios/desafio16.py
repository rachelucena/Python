dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilometros rodados? '))
p1 = dias * 60
p2 = km * 0.15
valor = p1 + p2
print('O total a pagar e de R${}'.format(valor))