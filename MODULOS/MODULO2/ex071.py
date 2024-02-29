while True:
    print('\033[31m ATENÇÃO!!\033[m Somente disponíveis notas de R$ 100 | R$ 50 | R$ 20 | R$ 10.')
    valor = int(input('Quanto deseja sacar? R$ '))
    total = valor
    nota = 100
    totalnotas = 0
    while True:
        if total>= nota:
            total = total - nota
            totalnotas = totalnotas + 1
        else:
            if totalnotas > 0:
                print(f'Total de {totalnotas} cédulas de R$ {nota}')
            if nota == 100:
                nota = 50
            elif nota == 50:
                nota = 20
            elif nota == 20:
                nota = 10
            totalnotas = 0
            if total == 0:
                break 
    sair = input('Deseja SAIR [S/N]? ').upper().strip()[0]
    while sair != 'S' and sair != 'N':
        sair = input('Deseja SAIR [S/N]? ').upper().strip()[0]
    if sair == 'S':
        break
