times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo',
         'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional',
         'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro',
         'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
print('*'*30)
print('\033[32mLISTA DE TIMES DO BRASILEIRÃO:\033[m\n')
print('*'*30)
for cont in times:
    print(cont)
print('*'*30)
print(f'Os 5 primeiros colocados são: {times[:5]}.')
print('*'*30)
print(f'Os 4 últimos colocados são: {times[-4:]}.')
print('*'*30)
print(f'Todos os times em ordem alfabética: ')
for list in sorted(times):
    print(list)
print('*'*30)
print(f'O FLUMINENSE está na {times.index("Fluminense")+1}ª posição.')
