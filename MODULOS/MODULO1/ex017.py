import math
oposto = float(input('Informe o comprimento do cateto oposto: '))
adjacente = float(input('Informe o comprimento do cateto adjacente: '))
'''hipo = (oposto ** 2 + adjacente ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipo))'''
hipo = math.hypot(oposto, adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipo))
