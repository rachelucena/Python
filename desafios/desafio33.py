n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
maior = n1
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n2
print('O menor valor e {}'.format(menor))
if n2>n1 and n3>n2:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O maior valor e {}'.format(maior))