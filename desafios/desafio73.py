times = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Sao Paulo', 'Internacional'
         'Bahia', 'Cruzeiro', 'Vasco da Gama', 'Atletico Mineiro', 'Gremio', 'Criciuma'
         'Bragantino', 'Juventude', 'Atletico Paranaense', 'Fluminense', 'Vitoria',
         'Corinthians', 'Cuiaba', 'Atletico Goianiense')
print('=-' * 30)
print(f'Lista de times do Brasileirao: {times}')
print('=-' * 30)
print(f'Os cinco primeiros colocados sao: {times[0:5]}')
print('=-' * 30)
print(f'Os quatro ultimos colocados sao: {times[-4:]}')
print('=-' * 30)
print(f'Os times em ordem alfabetica: {sorted(times)}')
print('=-' * 30)
print(f'O Cruzeiro esta na {times.index("Cruzeiro")+1} posicao')
