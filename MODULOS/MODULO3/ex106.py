from time import sleep

def ajuda(comando):
    help(comando)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('*' * tam)
    print(f'\033[0;30;41m  {msg}  \033[m')
    print('*' * tam)
    sleep(1)


txt = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    print('SISTEMA DE AJUDA PyHELP')
    txt = input('Função ou Biblioteca: ')
    sleep(1)
    if txt.upper().strip() == 'FIM':
        break
    else:
        ajuda(txt)
titulo('ATÉ BREVE!!  ')


