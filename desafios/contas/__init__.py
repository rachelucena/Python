def metade(n, format=False):
    return n / 2 if format is False else formatar_moeda(n)

def dobro(n, format=False):
    return n * 2 if format is False else formatar_moeda(n)

def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if format is False else formatar_moeda(res)

def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if format is False else formatar_moeda(res)

def porc(n):
    porc = n * 1.10
    return porc if format is False else formatar_moeda(n)

def formatar_moeda(valor):
    return f"R${valor:,.2f}".replace('.', ',')

def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preco analisado: \t{formatar_moeda(preco)}')
    print(f'Dobro do preco: \t{dobro(preco, True)}')
    print(f'Metade do preco: \t{metade(preco, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'Com {taxar}% de diminuicao: \t{diminuir(preco, taxar, True)}')
    print('-' * 30)