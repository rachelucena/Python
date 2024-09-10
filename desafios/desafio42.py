print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')
print('Analisador de triangulos')
print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a == b and b == c:
    print('Esse triangulo e EQUILATERO.')
elif a == b or a == c or b == c:
    print('Esse triangulo e ISOSCELES.')
elif a != b and a != c and c != b:
    print('Esse triangulo e ESCALENO.')
elif a+b < c or a+c < b or b+c < a:
    print('Os segmentos acima nao podem formar um triangulo.')