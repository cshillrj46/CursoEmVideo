from time import sleep

def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    if i > f:
        p *= -1
    
    print('Contagem de 1 até 10, de 1 em 1:')
    for cont in range(0, 10, 1):
        cont += 1
        print(f'{cont}', end=' ', flush=True)
        sleep(0.5)
    print('\n')
    
    print('Contagem de 10 até 0, de 2 em 2:')
    for cont in range(11, 0, -2):
        cont -= p
        print(f'{cont}', end=' ', flush=True)
        sleep(0.5)
    print('\n')

    print('Agora, personalize a contagem: ')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    for cont in range(i, f, p):
        cont *= 1
        print(f'{cont}', end=' ', flush=True)
        sleep(0.5)
    if i > f:
        for cont in range(i, f, -p):
            #cont -= p
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
    if p < 0:
        for cont in range(i, f, p):
            cont += p
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
    print('FIM')
    print('\n')
       
        
contador(0, 10, 1)
