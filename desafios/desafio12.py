larg = float(input('Largura da parede: '))
altu = float(input('Altura da parede: '))
area = larg * altu
latas = area / 2
print('Sua parede tem a dimensao de {}x{} e sua area e de {}m2'.format(larg, altu, area))
print('Voce precisara de {} latas de tinta'.format(latas))
