cont = man = menor = 0
sair = 'sn'
while True:
    idade = int(input('Digite sua idade: '))
    sexo = input('Informe seu sexo [ M ] ou [ F ]: ').upper().strip()[0]
    if sexo != 'MF':
            print('opção errada.')
    sair = str(input('Deseja SAIR [S/N]? ')).upper().strip()[0]
    if idade > 18:
        cont = cont + 1       
    if sexo == 'M':
        man = man + 1
    if sexo == 'F' and idade < 20:
        menor = menor + 1
    if sair == 'S':
        break      
print(f'{cont} pessoas tem mais de 18 anos.')    
print(f'{man} homens foram cadastrados.')
print(f'{menor} mulheres têm MENOS de 18 anos.')
