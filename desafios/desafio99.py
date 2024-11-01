import time
import random

def maior(* num):
    sorteio = [6, 3, 2, 1, 0]

    for i, quant_sorteio in enumerate(sorteio):
        if quant_sorteio > 0:
            num_sorteados = random.sample(range(11), quant_sorteio)
            maior_num = max(num_sorteados)
            print(f'Sorteio {i + 1} ({quant_sorteio} numeros): {num_sorteados} -> Maior numero: {maior_num}')
        else:
            print(f'Sorteio 5 (0 numeros): -> Maior numero: nao e possivel definir')

maior()

