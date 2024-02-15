from math import factorial
# FUNÇÕES

'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

# PROGRAMA PRINCIPAL
soma(10, 11)
soma(9, 9)


def contador(*num):
    tam = len(num)
    print(f'Valores: {num}, total: {tam}')

contador(2, 1, 5)
contador(1, 9, 6, 4)
contador(8, 7, 6)


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [7, 9, 4, 1, 3, 2]
dobra(valores)
print(valores)

def soma(* valores): # DESEMPACOTAMENTO
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores}, temos {s}')


soma(5, 7)
soma(2, 5, 9)

def fatorial(num=0):
    num = factorial(num)
    return num
    

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}')'''

def Par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False
    

num = int(input('Digite um número: '))
if Par(num):
    print('PAR')
else:
    print('ÍMPAR')
