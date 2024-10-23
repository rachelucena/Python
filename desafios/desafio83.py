expressao = input("Digite uma expressão matemática: ")
pilha = []

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')  # Adiciona parêntese aberto à pilha
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()  # Remove parêntese aberto correspondente
        else:
            pilha.append(')')  # Adiciona parêntese fechado se não houver aberto

if len(pilha) == 0:
    print("A expressão está correta!")
else:
    print("A expressão está incorreta!")