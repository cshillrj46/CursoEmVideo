total = cont = caro = barato = 0
menor = ''
sair = 'sn'
while True:
    produto = input('Informe o nome do produto: ')
    preco = float(input('Informe o valor do produto: R$ '))
    cont += 1
    total = total + preco
    sair = input('Deseja SAIR [S/N]? ').upper().strip()[0]
    if preco > 1000:
        caro += 1
    if cont == 1:
        barato = preco
        menor = produto
    else:
        if preco < barato:
            barato = preco
            menor = produto
    if sair == 'S':
        break
print(f'Você gastou o TOTAL de R$ {total:.2f}')
print(f'{caro} produtos custaram mais de R$ 1.000,00')
print(f'O produto {menor} foi o mais BARATO e custou R$ {barato:.2f}')
