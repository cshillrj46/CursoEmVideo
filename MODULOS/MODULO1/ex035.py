r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))
# PARA FORMAR UM TRIÂNGULO A SOMA DE DOIS LADOS DEVE SEMPRE SER MENOR QUE O TERCEIRO LADO
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os valores digitados podem formar um triângulo!')
else:
    print('Os valores digitados NÃO podem formar um triângulo!')
    