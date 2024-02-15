'''from math import factorial
num = 1
while num != 0:
    num = int(input('Digite um número: '))
    if num == 0:
        print('FIM')
    else:
        print('O fatorial do número digitado é {}'.format(factorial(num)))'''

#    OUTRA FORMA DE FAZER (INICIANTE) ###################################

num = int(input('Digite um número: '))
cont = num
fac = 1
while cont > 0:
    print('{}'.format(cont), end = '')
    print(' x ' if cont > 1 else ' : ', end = '')
    fac = fac * cont
    cont = cont - 1
print('O fatorial do número digitado é {}'.format(fac))
