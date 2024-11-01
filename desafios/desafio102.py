def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um numero.
    :param n: O numero a ser calculado.
    :param show: (opcional) mostra ou nao a conta.
    :return: O valor do fatorial de um numero n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(' x ', end="")
            else:
                print(' = ', end="")
        f *= c
    return f

print(fatorial(5, show=True))
help(fatorial)
