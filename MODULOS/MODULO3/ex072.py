num = ('zero', 'um', 'dois', 'três', 'quatro',
       'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
num2 = int(input('Digite um número entre 0 e 10: '))
while num2 < 0 or num2 > 10:
    print('OPÇÃO ERRADA')
    num2 = int(input('Digite um número de 0 à 10: '))
print(f'Você digitou o número {num[num2]}.')
