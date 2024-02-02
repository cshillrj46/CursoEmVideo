val = []
while True:
    val.append(int(input('Digite um valor: ')))
    sair = input('Deseja adicionar mais valores [S/N]? ').upper().strip()[0]
    if sair != 'SN':
        print('OPÇÃO ERRADA')
    val.sort(reverse=True)
    if sair == 'N':
        break
print(f'Foram digitados {len(val)} valores.')
print(f'Os valores digitados, em ordem decrescente, são: {val}')
if 5 in val:
    print('O número 5 faz parte da lista.')
else:
    print('O número 5 NÃO faz parte da lista.')
