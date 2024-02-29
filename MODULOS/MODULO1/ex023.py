'''num = input('Digite um número entre 0 e 9999: ')
print(num)
print('Unidade: {}'.format(num[3:]))
print('Dezena: {}'.format(num[2:3]))
print('Centena: {}'.format(num[1:3:2]))
print('Milhar: {}'.format(num[0]))

print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))'''

num = int(input('Digite um número entre 0 e 9999: '))
unidade = num // 1 % 10
dezenda = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezenda))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
