num = total = cont = 0
print('Para SAIR, digite 999.')
num = int(input('Digite um número:'))
while num != 999:
    total = total + num
    cont = cont + 1
    num = int(input('Digite um número:'))
print('Você digitou {} números e a soma deles é {}.'.format(cont, total))
