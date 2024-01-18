from random import randint
while True:
    num = int(input('Escolha um número: '))
    comp = randint(0, 10)
    total = num + comp
    jogo = ' '
    while jogo not in 'PI':
        jogo = input('Quer PAR ou ÍMPAR [P/I]? ').upper().strip()[0]
    print(f'Você jogou {num} e o computador jogou {comp}, que somados vale {total}.')
    if jogo == 'P':
        if total % 2 == 0:
            print('Deu PAR. Você VENCEU!!')
        else:
            print('Deu ÍMPAR. Você PERDEU!!')
            break
    elif jogo == 'I':
        if total % 2 == 1:
            print('Deu ÍMPAR. Você VENCEU!!')
        else:
            print('Deu PAR. Você PERDEU!!')
            break
        