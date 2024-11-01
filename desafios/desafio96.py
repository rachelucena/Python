def area(l, c):
    a = l * c
    return a

print('-' * 25)
print(f'   Controle de terrenos')
print('-' * 25)

l = float(input(f'Largura (m): '))
c = float(input(f'Comprimento (m): '))
a = area(l, c)
print(f'A area de um terreno {l:.2f}X{c:.2f} e de {a:.2f}m²')