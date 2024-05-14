preco = float(input('Qual o valor do produto? R$'))
desc = preco - (preco * 5) / 100
print(input('O poduto que custava R${}, na promocao com desconto de 5% vai custar R${}'.format(preco, desc)))