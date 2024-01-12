num = 0
total = 0
cont = 0
print('Para SAIR, digite 999.')
while num != 999:
    num = int(input('Digite um número:'))
    total = total + num
    cont = cont + 1
    if num == 999:
        total = total - 999
print('Você digitou {} números e a soma deles é {}.'.format(cont - 1, total))