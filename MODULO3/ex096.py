def area(comp, larg):
    med = comp * larg
    print(f'A área total do terreno é {med} m²')


larg  = float(input('Digite a largura do terreno: '))
comp = float(input('Digite o comprimento do terreno: '))
area(comp, larg)