from datetime import date
ano = int(input('Informe o ano desejado para saber se é bissexto: '))
if ano == 0:
    ano = date.today().year # PARA PEGAR SOMENTE O ANO ATUAL
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} NÃO é bissexto!'.format(ano))
