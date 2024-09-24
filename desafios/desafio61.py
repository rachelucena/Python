import time
print('Gerador de PA')
print('=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-')
pt = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
termo = pt
c = 1
while c <= 10:
    termo += razao
    c += 1
    print('{} '.format(termo), end='-> ')
    time.sleep(1)
print('FIM!')