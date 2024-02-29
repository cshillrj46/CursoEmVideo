num = int(input('Informe o primeiro termo da Progressão Aritmética: '))
raz = int(input('Informe a razão da PA: '))
termo = num
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end = '')
        termo = termo + raz
        cont = cont + 1
    print('PAUSA')
    mais = int(input('\nQuantos termos a mais você deseja? '))
print('{} termos mostrados na tela.'.format(total))
print('FIM')
