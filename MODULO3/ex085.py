lista = []
par = []
impar = []
for cont in range(0, 7):
    num = int(input(f'Digite o {cont + 1}º número: '))
    if num % 2 == 0:
        par.append(num)
        par.sort()
    elif num % 2 == 1:
        impar.append(num)
        impar.sort()
lista.sort()
lista.append(par[:])
lista.append(impar[:])
print(f'Valores PARES: {lista[0]}')
print(f'Valores ÍMPARES: {lista[1]}')
