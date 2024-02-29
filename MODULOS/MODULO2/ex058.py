from random import randint
from time import sleep
jogador = 1
computador = randint(0, 10)
palpite = 0
print(computador)
while jogador != computador:
    jogador = int(input('Qual o número que o computador escolheu (entre 0 e 10)? '))
    if palpite != computador:
        palpite = palpite + 1
    print('PROCESSANDO...')
    sleep(1)
print('O computador escolher o número {} e você deu {} palpites até acertar!'.format(computador, palpite))
print('FIM')
