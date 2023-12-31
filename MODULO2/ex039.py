from datetime import date
ano = int(input('Informe o ano em que você nasceu: '))
atual = date.today().year
alist = atual - ano
if alist == 18:
    print('Você deve alistar-se no serviço militar IMEDIATAMENTE.')
elif alist < 18:
    falta = 18 - alist
    print('Você tem {} anos. Faltam {} para o alistamento militar.'.format(alist, falta))
else:
    falta = alist - 18
    print('Você tem {} anos e já deveria ter feito seu alistamento militar há {} ano(s).'.format(alist, falta))
    