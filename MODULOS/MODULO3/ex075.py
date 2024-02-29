num = (int(input('Digite um número: ')), 
int(input('Digite outro número: ')), 
int(input('Digite mais um número: ')), 
int(input('Digite o último número: ')))
print(f'O número 9 foi digitado {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print('O número 3 não foi digitado.')
print('Os números PARES digitados foram: ', end=' ')
for cont in num:
    if cont % 2 == 0:
        print(cont, end=' ')
