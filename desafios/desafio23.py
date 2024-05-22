numero = int(input('Digite um numero: '))
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = numero // 1000
print("Unidade: {}".format(unidade))
print("Dezena: {}".format(dezena))
print("Centena: {}".format(centena))
print("Milhar: {}".format(milhar))