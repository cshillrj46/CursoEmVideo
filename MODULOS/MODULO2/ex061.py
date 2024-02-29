cont = 1
num = int(input('Informe o primeiro termo da Progressão Aritmética: '))
raz = int(input('Informe a razão da PA: '))
termo = num
while cont <= 10:
    print('{} - '.format(termo), end = '')
    termo = termo + raz
    cont = cont + 1
print('FIM')
