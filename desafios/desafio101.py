from datetime import datetime

def voto():
    idade = datetime.now().year - nasc
    if idade < 18 or idade > 70:
        print(f'Idade: {idade} anos\nVoto OPCIONAL!')
    else:
        print(f'Idade: {idade} anos\nVoto OBIGATORIO!')


nasc = int(input('Ano de nascimento: '))
voto()
