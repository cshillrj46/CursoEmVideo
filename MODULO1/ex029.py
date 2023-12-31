veloz = float(input('Informe a velocidade do veículo: '))
if veloz <= 80:
    print('O veículo passou na velocidade permitida, que é de 80 Km/h.')
else:
    multa = float(veloz - 80) * 7
    print('O veículo ultrapassou a velocidade permitida, que é de 80 Km/h')
    print('Você foi MULTADO no valor de R$ {:.2f}'.format(multa))
print('***** RESPEITE AS LEIS DE TRÂNSITO. *****')   