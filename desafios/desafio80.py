listanum = []
for c in range(0, 5):
    n = int(input(f'Digite um valor: '))
    if c == 0 or n > listanum[-1]:
        listanum.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(listanum):
            if n <= listanum[pos]:
                listanum.insert(pos, n)
                print(f'Adicionado na posição {pos}.')
                break
            pos += 1
print(f'Os valores digitados em ordem são: {listanum}')