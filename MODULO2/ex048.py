soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont = cont + 1 # Serve pra fazer a contagem 
        soma = soma + c # Serve pra somar tudo (acumulador)
print('Total de {} valores que somados valem {}.'.format(cont, soma))
