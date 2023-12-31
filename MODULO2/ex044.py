valor = float(input('Informe o preço do produto: R$ '))
print('Para pagamento à vista dinheiro/cheque. Digite [ 1 ]: ')
print('Para pagamento à vista no cartão de crédito. Digite [ 2 ]: ')
print('Para pagamento parcelado em até 2 vezes no cartão de crédito. Digite [ 3 ]: ')
print('Para pagamento parcelado em 3 vezes ou mais no cartão de crédito. Digite [ 4 ]: ')
choice = int(input('Sua OPÇÃO: '))
if choice == 1:
    dinheiro = valor - (valor * 10 / 100)
    print('O valor do produto para pagamento à vista em dinheiro/cheque é de R$ {:.2f}'.format(dinheiro))
elif choice == 2:
    card = valor - (valor * 5 / 100)
    print('O valor do produto para pagamento à vista no cartão de crédito é de R$ {:.2f}'.format(card))
elif choice == 3:
    par2 = valor
    print('O valor do produto parcelado em até 2 vezes no cartão de crédito é de R$ {:.2f}'.format(par2))
elif choice == 4:
    par3 = valor + (valor * 20 / 100)
    print('O valor do produto para parcelamento em 3 vezes ou mais no cartão de crédito é de R$ {:.2f}'.format(par3))
else:
    print('Você digitou a opção ERRADA.')
    