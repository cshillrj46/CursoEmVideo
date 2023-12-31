trip = float(input('Informe a distância em Km da sua viagem: '))
# val = trip * 0.50 if trip <= 200 else trip * 0.45 (FORMA SIMPLIFICADA OU TERNÁRIA)
if trip <= 200:
    val = trip * 0.50
    print('Sua passagem vai custar R$ {:.2f}'.format(val))
else:
    val = trip * 0.45
    print('Sua passagem vai custar R$ {:.2f}'.format(val))
print('***** BOA VIAGEM *****')