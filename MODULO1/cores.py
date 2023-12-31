print('\033[0;30;41mTESTE\033[m')
print('\033[4;34;44mTESTE\033[m')
print('\033[1;32;45mTESTE\033[m')
print('\033[7;36;47mTESTE\033[m')
a = 40
b = 50
print('Os valores são \033[1;33m{}\033[m e \033[1;35m{}\033[m.'.format(a, b))
texto = 'Olá, Mundo!'
print('A frase é: {}{}{}'.format('\033[1;33m', texto, '\033[m'))

# CRIAR LISTA DE CORES
cores = {'azul':'\033[34m',
         'amarelo':'\033[33m',
         'PretoeBranco':'\033[7;35m',
         'limpa':'\033[m'}

print('De novo: {}{}{}'.format(cores['PretoeBranco'], texto, cores['limpa']))
