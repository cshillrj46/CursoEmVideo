num1 = 0
num2 = 0
menu = 0
total = 0
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
while menu != 5:
    menu = int(input('''Escolha uma das opções:
        Para SOMAR         digite [1]:
        Para MULTIPLICAR   digite [2]:
        Para MAIOR         digite [3]:
        Para NOVOS NÚMEROS digite [4]:
        Para SAIR          digite [5]: '''))
    if menu == 1:
        total = num1 + num2
        print('A soma de {} e {} é igual a {}.'.format(num1, num2, total))
    elif menu == 2:
        total = num1 * num2
        print('{} multiplicado por {} é igual a {}.'.format(num1, num2, total))
    elif menu == 3:
        print('maior')
    elif menu == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
print('FIM') 
