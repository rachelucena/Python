import random
numero = random.randint(0, 10)
print('Ola! Eu sou seu computador!')
print('Acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegue adivinhar qual foi?')
palpite = int(input('Qual o seu palpite? '))
tentativa = 1
while palpite != numero:
    tentativa += 1
    if palpite < numero:
        print('Mais... Tente mais uma vez.')
        palpite = int(input('Qual o seu palpite? '))
    if palpite > numero:
        print('Menos... Tente mais uma vez.')
        palpite = int(input('Qual o seu palpite? '))
print('Parabens, voce acertou em {} tentativas.'.format(tentativa))