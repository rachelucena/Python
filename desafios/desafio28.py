import random
num = random.randint(0, 5)
print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=---=--=--=---=--=--=-')
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar!')
print('-=--=--=--=--=--=---=--=--=--=--=--=--=--=--=--=--=--=---=--=--=-')
n = int(input('Em que numero eu pensei? '))
if num == n:
    print('Parabens! Voce acertou!')
else:
    print('Eu pensei no numero {}. Nao foi dessa vez!'.format(num))
