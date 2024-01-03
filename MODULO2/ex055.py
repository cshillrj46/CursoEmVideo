maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Informe seu peso: '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O MAIOR peso é {} Kgs.'.format(maior))
print('O MENOR peso é {} Kgs.'.format(menor))
    