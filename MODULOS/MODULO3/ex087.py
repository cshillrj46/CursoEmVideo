matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = maior = somaColuna = 0
for linha in range (0, 3):
    for coluna in range (0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha} e {coluna}]: '))
for linha in range (0, 3):
    for coluna in range (0, 3):
        print(f'[ {matriz[linha][coluna] :^3} ]', end = '')
        if matriz[linha][coluna] % 2 == 0:
            somaPar += matriz[linha][coluna]
    print()
print(f'A soma dos valores PARES é: {somaPar}')
for linha in range (0, 3):
    somaColuna += matriz[linha][2]
print(f'A soma dos valores da 3ª coluna é: {somaColuna}')
for coluna in range (0, 3):
    if coluna == 0 or matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da 2ª linha é: {maior}')
