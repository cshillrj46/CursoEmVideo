valor = float(input('Informe o valor do produto: R$'))
desc = (valor * 5) / 100
total = valor - desc
print('O produto recebeu um desconto de 5% e você vai pagar R${:.2f}'.format(total))
