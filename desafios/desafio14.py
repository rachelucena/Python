salario = float(input('Qual o salario do funcionario? R$'))
aumento = salario + (salario * 15 / 100)
print('O funcionario que ganhava R${}, com 15% de aumento vai passar a ganhar R${}'.format(salario, aumento))