pessoas = {}
dados = []
soma = media = 0
while True:
    pessoas['nome'] = input('Informe o nome: ').upper().strip()
    while True:
        pessoas['sexo'] = input('Informe o sexo: ').upper().strip()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('OPÇÃO ERRADA')
    pessoas['idade'] = int(input('Informe a idade: '))
    soma = soma + pessoas['idade']
    while True:
        sair = input('Deseja continuar [S/N]? ').upper().strip()[0]
        if sair in 'SN':
            break
    dados.append(pessoas.copy())
    if sair == 'N':
        break
print(f'O grupo tem {len(dados)} pessoas.')
media = soma / len(dados)
#print(f'A soma das idades cadastradas é {soma}')
print(f'A média das idades cadastradas é {media:5.2f}')
print('As mulheres cadastradas foram: ', end='')
for mulher in dados:
    if mulher['sexo'] in 'F':
        print(f'{mulher["nome"]}', end=' ')
print()
print('Pessoas acima da média: ', end='')
for acima in dados:
    if acima['idade'] > media:
        print(f'{acima["nome"]}', end=' ')
