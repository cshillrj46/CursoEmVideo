nome = input('Digite seu nome completo: ').strip()  #elimina os espaços antes e depois
print(nome.upper())
print(nome.lower())
print(nome.split())
lista = (nome.split())
print('{} letras.'.format(len(lista[0])))
print('Total de {} letras.'.format(len(nome) - nome.count(' '))) # Dessa forma, deixa de contar o espaço no meio
print('O primeiro nome tem {} letras'.format(nome.find(' '))) # outra forma de contar as letras do primeiro nome
