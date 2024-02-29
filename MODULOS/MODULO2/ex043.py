altura = float(input('Informe sua altura: '))
altura = altura / 100
peso = float(input('Informe seu peso: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é {:.1f}: ABAIXO DO PESO'.format(imc))
elif imc <= 25:
    print('PESO IDEAL')
elif imc <= 30:
    print('Seu IMC é {:.1f}: SOBREPESO'.format(imc))
elif imc <= 40:
    print('Seu IMC é {:.1f}: OBESIDADE'.format(imc))
else:
    print('Seu IMC é {:.1f}: OBESIDADE MÓRBIDA'.format(imc))
    