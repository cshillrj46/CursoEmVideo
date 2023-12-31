import random
aluno1 = input('Digite o primeiro nome: ')
aluno2 = input('Digite o segundo nome: ')
aluno3 = input('Digite o terceiro nome: ')
aluno4 = input('Digite o último nome: ')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem de alunos escolhida foi: {}'.format(lista))
