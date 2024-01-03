soma = 0
cont = 0
for num in range(1, 7):
    num = int(input('Digite o {}º número:'.format(num)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('{} números PARES digitados.'.format(cont))
print('A soma de todos os números PARES é {}.'.format(soma))
