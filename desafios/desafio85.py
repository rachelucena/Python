numeros = list()
pares = list()
impares = list()

for c in range(1, 8):
    valor = int(input(f'Digite o {c}\u00BA valor: '))
    numeros.append(valor)

    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

pares.sort()
impares.sort()

print(f'=-' * 30)
print(f'Todos os valores digitados: {numeros}')
print(f'Os valores pares digitados: {pares}')
print(f'Os valores impares digitados: {impares}')