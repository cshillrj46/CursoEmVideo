somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
mulhermenos20 = 0
for c in range(1, 5):
    nome = input('Digite seu nome:').upper().strip()
    idade = int(input('Digite sua idade: '))
    sexo = input('Informe seu sexo [ M ] ou [ F ]: ').upper().strip()
    somaidade = somaidade + idade
    if c == 1 and sexo == 'M':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome         
    if sexo == 'F' and idade < 20:
        mulhermenos20 = mulhermenos20 + 1     
mediaidade = somaidade / 4    
print('A média das idades é {} anos'.format(mediaidade))    
print('{} é o homem mais velho e tem {} anos.'.format(nomemaisvelho, maioridadehomem))
print('{} mulheres tem MENOS de 20 anos.'.format(mulhermenos20))
