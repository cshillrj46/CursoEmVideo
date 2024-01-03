frase = input('Digite a frase: ').upper().strip()
word = frase.split() # SEPARA TUDO EM UMA LISTA
juntar = ''.join(word) # JUNTA TUDO EM UMA SÓ STRING



# DA PRA FAZER COM E SEM O "FOR"

inverter = juntar[:: -1]
print(inverter)

'''inverter = ''
for letra in range(len(juntar) - 1, - 1, - 1): # DA ÚLTIMA LETRA ATÉ A PRIMEIRA. para mostrar na tela de trás pra frente
    inverter = inverter + juntar[letra]'''
    
if inverter == juntar:
    print('A frase digitada é PALÍNDROMO.')
else:
    print('A frase digitada NÃO é PALÍNDROMO.')
    
