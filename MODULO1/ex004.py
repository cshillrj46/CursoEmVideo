info01 = input('Digite algo: ')
print('O tipo primitivo do que foi digitado é ',type(info01))
print('Somente espaço foi digitado?',info01.isspace())
print('É somente letra minúscula?', info01.islower())
print('É somente numérico?', info01.isnumeric())
print('É somente letra?', info01.isalpha())
print('É alfanumérico?', info01.isalnum())