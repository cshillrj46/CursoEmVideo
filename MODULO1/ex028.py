from random import randint
from time import sleep # FAZ UMA PAUSA NO PROCESSAMENTO
num = randint(0, 5) # ESCOLHER VALOR ENTRE 0 E 5
user = int(input('Qual o número que o computador escolheu (entre 0 e 5)? '))
print('PROCESSANDO...')
sleep(3)
if user == num:
    print('Meus parabéns!! Você acertou. O número escolhido foi {}'.format(num))
else:
    print('Você errou! O número escolhido foi {}. Tente de novo!'.format(num))
print('*' * 5, 'FIM', '*' * 5)
