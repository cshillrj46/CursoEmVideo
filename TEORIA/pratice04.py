for c in range(0, 10):
    print('Olá, Mundo!')
print('*' * 12)
print('FIM')
###########################
for c in range(0, 11):
    print(c)
print('FIM')
###########################
for c in range(10, 0, -1):
    print(c)
print('FIM')
############################
num = int(input('Digite um número: '))
for c in range(0, num + 1): # coloca o +1 pra aparecer o último número na tela.
    print(c)
print('FIM')
#############################
inicio = int(input('Que número quer começar? '))
passo = int(input('Quer pular quantos números? '))
fim = int(input('Quer terminar em que número?'))
for c in range(inicio, fim + 1, passo):
    print(c)
print('FIM')
#############################
s = 0
for c in range(0, 3):
    n = int(input('Digite um número: '))
    s = s + n #(s += n) outra forma de escrever
print('Total é {}'.format(s))
