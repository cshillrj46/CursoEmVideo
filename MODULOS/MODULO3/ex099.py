def maior(*valores):
    plus = 0
    for num in valores:
        num += 1
        plus = max(valores)
    if valores != 0:
        print(f'Foram informados {len(valores)} valores.')
        print(f'O maior valor é {plus}')
    elif valores == 0:
        print('Foi informado 0 valor.')


maior(9, 3, 6, 1, 7)
maior(5, 1, 3)
maior(6)
maior(0)