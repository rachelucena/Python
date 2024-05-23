print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')
print('Analisador de triangulos')
print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a+b > c or a+c > b or b+c > a:
    print('Os segmentos acima podem formar um triangulo.')
else:
    print('Os segmentos acima nao podem formar um triangulo.')