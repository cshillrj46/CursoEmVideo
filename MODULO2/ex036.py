casa = float(input('Informe o valor do imóvel desejado: R$ '))
salario = float(input('Informe o valor do seu salário atual: R$ '))
tempo = int(input('Informe em quantos anos você deseja pagar o financiamento: '))
meses = tempo * 12
parcela = casa / meses
pode = salario * 30 / 100
if parcela <= pode:
    print('O seu financiamento foi\033[1;33m APROVADO\033[m.')
elif parcela > pode:
    print('O seu financiamento foi\33[1;31m NEGADO\033[m.')
