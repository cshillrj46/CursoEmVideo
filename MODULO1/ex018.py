import math
# É necessário converter o valor do ângulo em graus para radiano
num = float(input('Informe o valor de um ângulo qualquer: '))
num = math.radians(num)
sen = math.sin(num)
cos = math.cos(num)
tan = math.tan(num)
print('o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(sen, cos, tan))
