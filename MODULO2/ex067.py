while True:
    num = int(input('Digite um valor: '))
    if num < 0:
        break
    for cont in range(1, 11):
        result = cont * num
        print(f'{num} x {cont:2} = {result:2}')
    