# DICIONÁRIOS

'''pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') # AQUI DEVE USAR ASPAS DUPLAS!
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for k, v in pessoas.items():
    print(f'{k}: {v}')

brasil = []
estado1 = {'Estado':'Rio de Janeiro', 'Sigla':'RJ'}
estado2 = {'Estado':'São Paulo', 'Sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)'''

estado = {}
brasil = []
for cont in range(0, 3):
    estado['Nome'] = input('Informe o Estado: ')
    estado['Sigla'] = input('Informe a sigla desse Estado: ')
    brasil.append(estado.copy())
print(brasil)
'''for e in brasil:
    print(e)
    for k, v in e.items():
        print(f'{k} : {v}')'''
