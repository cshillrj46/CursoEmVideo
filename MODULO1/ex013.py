valor = float(input('Informe o seu salário: R$'))
bonus = (valor * 15) / 100
total = valor + bonus
print('Você recebeu um aumento de 15% e seu novo salário é de R${:.2f}'.format(total))
