valores = []
sair = 'SN'
while True:
    num = int(input('Digite um número: '))
    if num not in valores:
        valores.append(num)
    else:
        print('Valor já digitado!!')
    sair = input('Deseja digitar outro valor [S/N]? ').upper().strip()[0]
    if sair == 'N':
        break
valores.sort()
print(f' A lista criada foi: {valores}.')    
