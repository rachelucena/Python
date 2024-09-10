num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversao: 
      [1] converter para BINARIO
      [2] converter para OCTAL
      [3] converter para HEXADECIMAL''')
opcao = int(input('Sua opcao: '))
if opcao == 1:
    print('{} convertido para BINARIO e igual a {}'.format(num, bin(num)))
elif opcao == 2:
    print('{} convertido para OCTAL e igual a {}'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL e igual a {}'.format(num, hex(num)))
else:
    print('Digite uma opcao valida')