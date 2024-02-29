import random
from time import sleep
print('Vamos brincar de PEDRA, PAPEL e TESOURA?!!')
choice = input('Digite a sua opção: ').upper() .strip()
pedra = 'PEDRA'
papel = 'PAPEL'
tesoura = 'TESOURA'
lista = [pedra, papel, tesoura]
computador = random.choice(lista)
print('*' * 54)
print('O COMPUTADOR escolheu {} e você escolheu {}.'.format(computador, choice))
print('*' * 54)
if choice == pedra and computador == pedra:
    print('PEDRA bate na PEDRA! EMPATOU.')
elif choice == pedra and computador == papel:
    print('PAPEL embrulha a PEDRA! O COMPUTADOR ganhou!!')
elif choice == pedra and computador == tesoura:
    print('PEDRA quebra TESOURA! Você GANHOU!!')
elif choice == papel and computador == papel:
    print('Os dois escolheram PAPEL. EMPATOU!!')
elif choice == papel and computador == pedra:
    print('PEDRA embrulha PAPEL. VOCÊ GANHOU!!')
elif choice == papel and computador == tesoura:
    print('TESOURA corta PAPEL. O COMPUTADOR ganhou!!')
elif choice == tesoura and computador == pedra:
    print('PEDRA quebra TESOURA. O COMPUTADOR ganhou!!')
elif choice == tesoura and computador == papel:
    print('TESOURA corta PAPEL. Você GANHOU!!')
elif choice == tesoura and computador == tesoura:
    print('Os dois escolheram TESOURA. EMPATOU!!')
else:
    print('VOCÊ ESCOLHEU A OPÇÃO ERRADA!!')
