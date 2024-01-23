# TUPLAS
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
pessoa = ('Cristiano', 46, 'Masc', 81)
print(sorted(lanche))
print(type(lanche))
print(lanche[1:3])
print(lanche[:2])
print(lanche[-1])
# AS TUPLAS SÃO IMUTÁVEIS
for comida in lanche:
    print(f'Eu vou comer {comida}.')

for cont in range(0, len(lanche)):
    print(lanche[cont])

while True:
    print(lanche)
    if lanche > lanche[:3]:
        break

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
