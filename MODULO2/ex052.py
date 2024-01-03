
num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    #print('{}'.format(c), end = ' - ')
    if num % c == 0 and num % num == 0:
        print('\033[33m{}\033[m'.format(c), end = ' ')
        total = total + 1
    else:
        print('\033[31m{}\033[m'.format(c), end = ' ')
print('\nO número {} foi divisível {} vezes.'.format(num, total))  
if total == 2: # Feito isso pra mostrar que é primo!!
    print('O número digitado é PRIMO.')
