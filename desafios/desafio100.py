from random import randint
from time import sleep

def sorteia(lista):
    print(f'Sorteando 5 valores para a lista: ', end="")
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end="", flush=True)
        sleep(0.5)

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares de {lista}, temos {soma}.')

numeros = list()
sorteia(numeros)
somapar(numeros)
