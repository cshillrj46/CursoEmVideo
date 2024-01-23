palavras = ('casa', 'vida', 'borboleta', 'jiboia', 'comprar', 'abacate')
for parte in palavras:
    print(f'\nNa palavra {parte} temos as vogais ', end='')
    for letra in parte:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')