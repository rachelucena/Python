valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salario? R$'))
ano = int(input('Quantos anos de financiamento? '))
fin = ano * 12
prest = valor / fin
porc = 30 / 100 * salario
if prest < porc or prest == porc:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestacao sera de R${:.2f}. EMPRESTIMO APROVADO!'.format(valor, ano, prest))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestacao sera de R${:.2f}. EMPRESTIMO NEGADO!'.format(valor, ano, prest))