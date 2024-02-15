def ficha(nome=0, gols=0):
    nome = input('Digite o nome do jogador: ').upper().strip()
    if nome == '':
        nome = '<Desconhecido>'
    gols = input('Número de gols feitos: ')
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print(ficha())