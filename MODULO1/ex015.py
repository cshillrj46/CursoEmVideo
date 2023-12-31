dia = int(input('Informe quantos dias você usou o veículo: '))
km = float(input('Informe o Km rodado pelo veículo: '))
valkm = km * 0.15
rentdias = dia * 60
total = valkm + rentdias
print('O valor total da locação é R${:.2f}'.format(total))
