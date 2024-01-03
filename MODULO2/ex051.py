num = int(input('Informe o primeiro termo da Progressão Aritmética: '))
raz = int(input('Informe a razão da PA: '))
decimo = num + (10 - 1) * raz
for num in range(num, decimo + raz, raz):
    print(num, end = ' - ')
print('FIM')
 