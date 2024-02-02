# AULA DE LISTAS
'''num = [6,3,8,9,2]
#num[2] = 0
num.sort(reverse=True)
num.append(7)
num.insert(2, 4)
num.pop(2)
num.remove(6)
print(num)
for pos, v in enumerate(num):
    print(f'Na posição {pos} está o número {v}.')
#*******************************************************************************************
lista = []
for cont in range(0, 5):
    lista.append(int(input('Digite um número: ')))
print(lista)
#*******************************************************************************************
a = [7, 6, 5, 4, 3, 2]
b = a[:]     # Colocando esses dois pontos dentro dos colchetes, apenas é criada a cópia da lista. Sem isso, A e B ficaram unidas e o que muda em uma, também muda na outra.
b[2] = 8
print(a)
print(b)'''
# *****************************    LISTA COMPOSTA   *****************************************
geral = []
pessoas = []
while True:
    pessoas.append(input('Nome: ').upper().strip())
    pessoas.append(int(input('Idade: ')))
    sair = input('Deseja sair? ').upper().strip()[0]
    geral.append(pessoas[:])
    pessoas.clear()
    if sair in 'S':
        break
print(geral)
for cont in geral:
    print(f'{cont[0]} tem {cont[1]} anos.')
