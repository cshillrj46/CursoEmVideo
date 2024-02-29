gols = []
dados = {'nome': '', 'gols': gols, 'total': 0}
dados['nome'] = input('Nome: ').upper().strip()
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for cont in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {cont + 1}? ')))
dados['total'] = sum(gols)
print(dados)
print('*' * 40)
print(f'Nome do jogador: {dados["nome"]}')
print(f'Gols feitos em cada partida jogada: {dados["gols"]}')
print(f'Total de gols feitos: {dados["total"]}')
print('*' * 40)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas:')
for pos, val in enumerate(gols):
    print(f'Na {pos + 1}ª partida, fez {val} gols.')
print(f'Total: {dados["total"]} gols.')
