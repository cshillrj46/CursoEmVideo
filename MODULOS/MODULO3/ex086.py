matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range (0, 3):
    for coluna in range (0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha} e {coluna}]: '))
for linha in range (0, 3):
    for coluna in range (0, 3):
        print(f'[ {matriz[linha][coluna] :^3} ]', end = '')
    print()