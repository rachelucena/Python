num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite mais um numero: '))
num4 = int(input('Digite o ultimo numero: '))
numeros = (num1, num2, num3, num4)
print(f'Voce digitou os valores {numeros}')
print(f'O valor 9 foi digitado {numeros.count(9)} vez(es).')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1} posicao.')
else:
    print(f'O valor 3 nao foi digitado.')
print(f'Os valores pares digitados foram {num}', end=' ')
pares = False
for num in numeros:
    if num % 2 == 0:
        print(num, end=' ')
        pares = True
if pares:
    print()
else:
    print(f'Nenhum valor par foi digitado.')


