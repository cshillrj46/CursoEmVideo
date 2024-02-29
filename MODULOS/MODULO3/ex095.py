time = []
gols = []
dados = {}
while True:
    dados.clear()
    dados['nome'] = input('Nome: ').upper().strip()
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    gols.clear()
    for cont in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {cont + 1}? ')))
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    time.append(dados.copy())
    while True:
        sair = input('Deseja continuar [S/N]? ').upper().strip()[0]
        if sair in 'SN':
            break
        print('OPÇÃO ERRADA')
    if sair == 'N':
        break 
print(time)
print('*' * 40)
print('COD.', end='')
for index in dados.keys():
    print(f'{index:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Digite o código do jogador para ver os dados (999 para SAIR): '))
    if busca == 999:
        break
    if busca > len(time):
        print('OPÇÃO ERRADA')
    else:
        print(f'Dados do jogador {time[busca]["nome"]}:')
        for index, feitos in enumerate(time[busca]['gols']):
            print(f'    Na {index + 1}ª partida fez {feitos} gols')
        