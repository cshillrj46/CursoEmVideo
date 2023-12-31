sal = float(input('Informe o valor do seu salário: R$ '))
if sal > 1250:
    novoSal = (sal * 10 / 100) + sal
    print('Você recebeu um aumento de 10 % e seu salário passou para R$ {:.2f}'.format(novoSal))
else:
    novoSal = (sal * 15 / 100) + sal
    print('Você recebeu um aumento de 15 % e seu salário passou para R$ {:.2f}'.format(novoSal))
print('***** FIM *****')
