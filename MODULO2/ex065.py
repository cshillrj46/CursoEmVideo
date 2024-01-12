num = 0
cont = 0 
media = 0
total = 0
sair = ''
while sair != 'S':
    num = int(input('Digite um número: '))
    sair = str(input('Deseja SAIR [ S/N ]? ')).upper().strip()
    cont = cont + 1
    total = total + num
    media = total / cont
print('A média dos valores digitados é {}.'.format(media))
