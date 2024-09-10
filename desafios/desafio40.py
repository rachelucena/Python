n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 7:
    print('Tirando {} e {}, a media do aluno e {}. O aluno esta REPROVADO!'.format(n1, n2, media))
elif media > 7 or media == 7:
    print('Tirando {} e {}, a media do aluno e {}. O aluno esta APROVADO!'.format(n1, n2, media))