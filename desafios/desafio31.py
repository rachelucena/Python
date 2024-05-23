dist = float(input('Qual a distancia da sua viagem? '))
preco = float
if dist <= 200:
    preco = dist * 0.50
    print('O valor da sua viagem sera de R$ {}'.format(preco))
else:
    preco = dist * 0.45
    print('O valor da sua viagem sera de R$ {}'.format(preco))