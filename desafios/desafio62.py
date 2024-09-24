import time
print('Gerador de PA')
print('=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-')
pt = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
termo = pt
total = 10
c = 1
while total != 0:
    while c <= total:
        print('{} '.format(termo), end='-> ')
        termo += razao
        c += 1
        time.sleep(1)
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
    if mais == 0:
        break
    else:
        total += mais
