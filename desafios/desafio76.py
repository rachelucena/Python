produtos = (
    ("Arroz", 5.99),
    ("Feijão", 4.50),
    ("Macarrão", 2.99),
    ("Açúcar", 3.25),
    ("Sal", 1.50),
)

# Exibindo o cabeçalho da tabela
print(f"{'Produto':<20} {'Preço (R$)':<10}")
print("-" * 30)

# Exibindo os produtos e seus preços
for produto, preco in produtos:
    print(f"{produto:<20} {preco:<10.2f}")  # Formata o preço com 2 casas decimais

print()  # Para adicionar uma nova linha após a listagem