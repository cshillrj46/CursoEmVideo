
def leiaInt():
    try:
        num = int(input('Digite um número inteiro: '))

    except:
        print('Você digitou algo ERRADO!')

    else:
        print(f'Você digitou o número {num}')

    
   
n = leiaInt()

def leiaFloat():
    try:
        num = float(input('Digite um número REAL: '))

    except:
            print('Você digitou um número ERRADO!')

    else:
        print(f'Seu número REAL é {num}')


num = leiaFloat()
