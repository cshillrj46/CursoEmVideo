def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número VÁLIDO.\033[m')
            continue
        except KeyboardInterrupt:
            print('Usuário não informou valor.')
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    cont = 1
    for item in lista:
        print(f'{cont} - {item}')
        cont += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc
