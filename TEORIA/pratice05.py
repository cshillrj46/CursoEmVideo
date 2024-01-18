c = 1
while c <= 10:
    print(c)
    c = c + 1

'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
print('{} números pares e {} números ímpares.'.format(par, impar))'''

n =s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s + n
#print('A soma dos valores é {}.'.format(s))
print(f'A soma dos valores é {s}.')  # atualizado no python 3.6