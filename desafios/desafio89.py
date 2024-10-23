alunos = []
while True:
    nome = str(input(f'Nome: '))
    nota1 = float(input(f'Nota 1: '))
    nota2 = float(input(f'Nota 2: '))

    media = nota1 + nota2 / 2

    alunos.append([nome, media])

    resp = str(input(f'Voce quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'NOME            MEDIA')
print(f'-' * 30)
for aluno in alunos:
    print(f'Nome: {aluno[0]}      Media: {aluno[1]:.2f}')