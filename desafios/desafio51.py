import time
print('------------------------------------')
print('        TERMOS DE UMA PA')
print('------------------------------------')
pt = int(input('Digite o primeiro termo: '))
razao = int(input('Razao: '))
decimo = pt + (10 - 1) * razao
for c in range(pt, decimo, razao):
    print('{} '.format(c), end='-> ')
    time.sleep(1)
print('ACABOU!')