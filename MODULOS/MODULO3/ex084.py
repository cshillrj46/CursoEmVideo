pessoas = []
cadastro = []
pesado = leve = 0
while True:
    pessoas.append(input('Digite o nome: '))
    pessoas.append(float(input('Digite o peso: ')))
    if len(cadastro) == 0:
        pesado = leve = pessoas[1]
    else:
        if pessoas[1] > pesado:
            pesado = pessoas[1]
        if pessoas[1] < leve:
            leve = pessoas[1]
    cadastro.append(pessoas[:])
    pessoas.clear()
    sair = input('Deseja continuar [S/N]? ').upper().strip()[0]
    if sair in 'N':
        break
print(f'Cadastrados: {len(cadastro)} pessoas.')
for cont in cadastro:
    if cont[1] == pesado:
        print(f'{cont[0]}', end=' | ')
print(f': O maior peso é: {pesado} kgs.')
for cont in cadastro:
    if cont[1] == leve:
        print(f'{cont[0]}', end=' | ')
print(f': O menor peso é: {leve} kgs.')
