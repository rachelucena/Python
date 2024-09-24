print('-------------------------')
print('Sequencia de Fibonacci')
n = int(input('Quantos termos da sequencia de Fibonacci voce quer mostrar? '))
termo1 = 0
termo2 = 1
contador = 1
while contador <= n:
    print('{} '.format(termo1), end=' ')
    prox_termo = termo1 + termo2
    termo1 = termo2
    termo2 = prox_termo
    contador += 1
