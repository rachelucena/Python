import random
n1 = str(input('Digite um nome: '))
n2 = str(input('Digite outro nome: '))
n3 = str(input('Digite mais um nome: '))
n4 = str(input('Digite um ultimo nome: '))
nomes = [n1, n2, n3, n4]
sorteio = random.choice(nomes)
print('O nome sorteado foi {}'.format(sorteio))