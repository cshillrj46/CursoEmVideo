soma = quant = media = maior = menor = 0 
sair = ''
while sair != 'S':
    num = int(input('Digite um número: '))
    sair = str(input('Deseja SAIR [ S/N ]? ')).upper().strip()[0]
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / quant
print('A média dos valores digitados é {:.2f}.'.format(media))
print('O valor menor é {} e o maior é {}.'.format(menor, maior))
