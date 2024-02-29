from random import randint
from time import sleep
mega = []
totaljogos = []
jogos = int(input('Quantos jogos você deseja? '))
total = 1
while total <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in mega:
            mega.append(num)
            cont += 1
        if cont >= 6:
            break
    mega.sort()
    totaljogos.append(mega[:])
    mega.clear()
    total += 1
print('JOGOS SORTEADOS:')
for index, list in enumerate(totaljogos):
    sleep(1)
    print(f'JOGO {index + 1}: {list}')
