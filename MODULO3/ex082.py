valores = []
par = []
impar = []
while True:
    valores.append(int(input('Digite um valor: ')))
    sair = input('Deseja adicionar mais valores [S/N]? ').upper().strip()[0]
    if sair == 'N':
        break
for pos, val in enumerate(valores):
    if val % 2 == 0:
        par.append(val)
    if val % 2 == 1:
        impar.append(val)
print(f'A lista completa é: {valores}')
print(f'A lista de números PARES é: {par}')
print(f'A lista de números ÍMPARES é: {impar}')
    