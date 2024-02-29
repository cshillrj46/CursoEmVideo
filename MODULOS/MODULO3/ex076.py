produtos = ('Caderno', 15.00, 'Caneta', 8.50, 'Borracha', 3.50,
            'Livro', 50.00, 'Lápis de cor', 75.00, 'Lapiseira', 17.50,
            'Camisa', 49.90, 'Bermuda', 59.90)
print('-'*40)
print(f'{"Listagem de produtos":^40}')
print('-'*40)
for pos in range (0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R$ {produtos[pos]:>5.2f}')