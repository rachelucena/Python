n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite um outro numero inteiro: '))
n3 = int(input('Digite um outro numero inteiro: '))
n4 = int(input('Digite um outro numero inteiro: '))
n5 = int(input('Digite um outro numero inteiro: '))
n6 = int(input('Digite um outro numero inteiro: '))
num = [n1, n2, n3, n4, n5, n6]
s = 0
for c in num:
    if c % 2 == 0:
        s += c
print('A soma de todos os valores pares e {}'.format(s))