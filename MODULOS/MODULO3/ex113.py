
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número VÁLIDO.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Usuário não informou valor.')
        else:
            return n
        

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número VÁLIDO.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Usuário não informou valor.')
        else:
            return n


num = leiaInt('Digite um número INTEIRO: ')
num2 = leiaFloat('Digite um número REAL: ')
print(f'O número INTEIRO digitado foi {num} e o REAL foi {num2}')
