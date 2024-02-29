from datetime import date
atual = date.today().year
data = int(input('Informe o ano de seu nascimento: '))
idade = atual - data
if idade <= 9:
    print('Você tem {} anos e sua categoria é MIRIM.'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e sua categoria é INFANTIL.'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e sua categoria é JÚNIOR.'.format(idade))
elif idade <= 25:
    print('Você tem {} anos e sua categoria é SÊNIOR.'.format(idade))
else:
    print('Você tem {} anos e sua categoria é MASTER.'.format(idade))