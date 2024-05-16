import math
a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))
c = math.sqrt(a ** 2 + b ** 2)
print('A medida da hipotenusa e: {}'.format(c))