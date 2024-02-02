valores = []
for cont in range(0 , 5):
    valores.append(int(input(f'Digite um número para a posição {cont}: ')))
print(f'O menor valor digitado foi {min(valores)}, nas posições ', end='')
for ind, val in enumerate(valores):
    if val == min(valores):
        print(f'{ind}...', end='')
print(f'\nO maior valor digitado foi {max(valores)}, na posição ', end='')
for ind, val in enumerate(valores):
    if val == max(valores):
        print(f'{ind}...', end='')
