sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    if sexo != 'M' and sexo != 'F':
        print('OPÇÃO ERRADA')
print('FIM')