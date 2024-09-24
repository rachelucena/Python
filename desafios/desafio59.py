v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
opcao = 0
maior =0
while opcao != 5:
    print('\n[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos numeros')
    print('[ 5 ] Sair do programa\n')
    opcao = int(input('Qual a sua opcao? '))
    if opcao == 1:
        soma = v1 + v2
        print('A soma de {} e {} e igual a {}.'.format(v1, v2,soma))
    elif opcao == 2:
        mult = v1 * v2
        print('A multiplicacao entre {} e {} e igual a {}.'.format(v1, v2, mult))
    elif opcao == 3:
       if v1 > v2:
           maior = v1
           print('O maior numero entre {} e {} e {}..'.format(v1, v2, maior))
       elif v2 > v1:
           maior = v2
           print('O maior numero entre {} e {} e {}.'.format(v1, v2, maior))
    elif opcao == 4:
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Fim do programa. Volte sempre!')
    else:
        print('Digite uma opcao valida.')



