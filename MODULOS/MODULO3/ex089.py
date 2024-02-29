dados = []
while True:
    nome = input('Digite o nome: ').upper().strip()
    nota1 = float(input('Digite a 1ª nota: '))
    nota2 = float(input('Digite a 2ª nota: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    sair = input('Deseja continuar [S/N] ?').upper().strip()[0]
    if sair == 'N':
        break
print(f'\033[33m{"Nº":<4}{" NOME":<12}{"MÉDIA":>10}\033[m')
for index, aluno in enumerate(dados):
    print(f'{index:<4} {aluno[0]:<10} {aluno[2]:>8.1f}')
while True:
    choice = int(input('Informe o número do aluno que deseja ver as notas: '))
    if choice == 999:
        break
    if choice <= len(dados) - 1:
        print(f'{dados[choice][0]}: Notas {dados[choice][1]}')
