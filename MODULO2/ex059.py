menu = 0
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
        if num1 > num2:
            maior = num1
            print('{} é o número maior.'.format(maior))
        elif num1 == num2:
            print('Os números digitados são \033[33mIGUAIS\033[m.')
        else:
            maior = num2
            print('{} é o número maior.'.format(maior))
    elif menu == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    elif menu == 5:
        print('FIM')
    else:
        print('OPÇÃO ERRADA.')
