cont = total = 0
print('Para SAIR, digite 999: ')
num = int(input('Digite um número: '))
while True:
    cont += 1
    total += num
    num = int(input('Digite um número: '))
    if num == 999:
        break
print(f'Você digitou {cont} valores e a soma deles é {total}.')
