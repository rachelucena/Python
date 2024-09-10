peso = float(input('Qual seu peso (KG)? '))
altura = float(input('Qual sua altura (m)? '))
imc = peso / (altura * altura)
print('O IMC dessa pessoa e {:.1f}'.format(imc))
if imc < 18.5:
    print('Essa pessoa esta abaixo do peso')
elif 18.5 <= imc < 25:
    print('Essa pessoa esta com o peso ideal')
elif 25 <= imc < 30:
    print('Essa pessoa esta com sobrepeso')
elif 30 <= imc < 40:
    print('Essa pessoa esta com obesidade')
else:
    print('Essa pessoa esta com obesidade morbida')