contador = 0
numero = 0
soma = 0
while numero != 999:
    numero = int(input('Digite um numero [999 para parar]: '))
    if numero != 999:
        soma += numero
        contador += 1
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(contador, soma))

