
def aumentar(preco=0, taxa=0, formato=False):
    mais10 = (preco * taxa) / 100
    novo = preco + mais10
    return novo if formato is False else moeda(novo)

def diminuir(preco=0, taxa=0, formato=False):
    menos13 = (preco * taxa) / 100
    novo = preco - menos13
    return novo if formato is False else moeda(novo)

def dobro(preco=0, formato=False):
    mais2x = preco * 2
    return mais2x if not formato else moeda(mais2x)

def metade(preco=0, formato=False):
    met = preco / 2
    return met if not formato else moeda(met)

def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:.2f}'.replace('.', ',')

def resumo(preco, taxaA=10, taxaR=5):
    print('*' * 30)
    print('RESUMO DOS VALORES'.center(30))
    print('*' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'O dobro do preço: \t{dobro(preco, True)}')
    print(f'A metade do preço: \t{metade(preco, True)}')
    print(f'Com {taxaA}% de aumento: \t{aumentar(preco, taxaA, True)}')
    print(f'Com {taxaR}% de redução: \t{diminuir(preco, taxaR, True)}')
    print('*' * 30)
