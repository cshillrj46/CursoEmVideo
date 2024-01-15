cont = 1
num = int(input('Quantos termos quer mostrar? '))
termo = num
termo1 = 0
termo2 = 1
termo3 = termo1 + termo2
print('{} - {}'.format(termo1, termo2), end = '')
cont = 3
while cont <= num:
    termo3 = termo1 + termo2
    print(' - {}'.format(termo3), end = '')
    termo1 = termo2
    termo2 = termo3
    cont = cont + 1
print(' - FIM')
