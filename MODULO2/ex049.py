num = int(input('Quer tabuada de quanto: '))
for c in range(1, 10 + 1):
    r = c * num
    print('{} x {:2} = {:2}'.format(num, c, r))
