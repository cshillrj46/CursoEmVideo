ficha = {}
dados = []
ficha['Nome'] = input('Digite o nome: ').upper().strip()
ficha['media'] = float(input('Informe a média: '))
dados.append(ficha.copy())
if ficha["media"] < 7.0:
    ficha['situação'] = 'REPROVADO'
else:
    ficha['situação'] = 'APROVADO'
for k, v in ficha.items():
    print(f'{k} é {v}')
