from datetime import date
menor = 0
maior = 0
for c in range(1, 8):
    data = int(input('Informe o ano que você nasceu: '))
    ano = date.today().year
    idade = ano - data
    if idade < 21:
        menor = menor + 1
    else:
        maior = maior + 1
print('{} pessoas NÃO atingiram a MAIOR IDADE, que é 21 anos'.format(menor))
print('{} pessoas atingiram a MAIOR IDADE.'.format(maior))
    