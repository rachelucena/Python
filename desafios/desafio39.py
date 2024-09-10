from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
if idade < 18:
    restante = 18 - idade
    print('Voce tem {} anos e faltam {} anos para voce poder se alistar.'.format(idade, restante))
elif idade == 18:
    print('Voce tem {} anos e deve se alistar ainda esse ano.'.format(idade))
else:
    passado = idade - 18
    print('Voce tem {} anos e se alistou ha {} anos.'.format(idade, passado))