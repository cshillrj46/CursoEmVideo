from math import factorial

def fatorial(n=0, show=False):
    if show == False:
        f = factorial(n)
        return(f)
    if show == True:
        f = factorial(n)
        cont = num
        while cont > 0:
            cont -= 1
            print(f'{cont + 1}', end=' ')
            print('x' if cont > 0 else '=', end=' ')
        return(f)
        

num = int(input('Digite um número: '))
print(fatorial(num, True))
