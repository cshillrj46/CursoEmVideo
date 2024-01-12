from math import factorial
num = 1
while num != 0:
    num = int(input('Digite um número: '))
    if num == 0:
        print('FIM')
    else:
        print('O fatorial do número digitado é {}'.format(factorial(num)))
        