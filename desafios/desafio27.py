n = str(input('Qual seu nome? ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome e {}'.format(nome[0]))
print('Seu ultimo nome e {}'.format(nome[len(nome)-1]))

