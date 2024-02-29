# EXEMPLO SIMPLES PARA MOSTRAR MODULARIZAÇÃO EM PYTHON

import uteis

num = int(input('Digite um número: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro o de {num} é {uteis.dobro(num)} e o triplo é {uteis.triplo(num)}.')