def leiaInt(num=0):
    ok = False
    valor = 0
    while True:
        num = input('Digite um número: ')
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[1;31mERRO! Digite um número válido.\033[m')
        if ok:
            break
    return(num)


n = leiaInt()
print(f'Você acabou de digitar o número {n}.')
