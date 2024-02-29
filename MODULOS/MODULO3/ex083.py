termo = input('Digite a expressão desejada: ')
lista = []
for simbol in termo:
    if simbol == '(':
        lista.append('(')
    elif simbol == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão é VÁLIDA!')
else:
    print('Expressão INVÁLIDA!!')
