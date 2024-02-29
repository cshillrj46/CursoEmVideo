num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
# VERIFICAR MENOR VALOR
menor = num1 # JÁ DIGO QUE O "num1" É O MENOR, PRA SIMPLIFICAR
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print('O menor número é o {}'.format(menor))
maior = num1 # JÁ DIGO QUE O "num1" É O MAIOR, PRA SIMPLIFICAR
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('O maior número é o {}'.format(maior))
