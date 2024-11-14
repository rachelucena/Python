from bli.interface import *
from time import sleep
from bli.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opcao de listar o conteudo de um arquivo
        lerarquivo(arq)
    elif resposta == 2:
        # Opcao para cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema. Ate logo!')
        break
    else:
        print('\033[31mERRO! Digite um opcao valida!\033[m')
    sleep(2)
