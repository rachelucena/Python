sal = float(input('Qual o salario do funcionario? R$'))
novosal = float
if sal <= 1250:
    novosal = sal + (sal * 15) / 100
    print('O novo salario sera de R${}'.format(novosal))
if sal > 1250:
    novosal = sal + (sal * 10) / 100
    print('O novo salario sera de R${}'.format(novosal))