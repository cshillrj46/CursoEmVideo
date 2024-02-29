from random import randint
numeros = []

def sorteia(numeros):
    """
    -> Função criada na aula de funções do Curso em Vídeo.
    """
    for cont in range(0, 5):
        num = randint(0, 10)
        numeros.append(num)
    print('Foram sorteados os números: ', end='')
    print(numeros)

def somaPar(numeros):
        soma = 0
        for p in numeros:
            if p % 2 == 0:
                soma += p
        print('A soma dos números PARES sorteados é: ', end='')
        print(soma)


sorteia(numeros)
somaPar(numeros)

help(sorteia)