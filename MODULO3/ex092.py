from datetime import date
dados = {}
dados['nome'] = input('Nome: ').upper().strip()
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
age = atual - nasc
dados['idade'] = age
dados['CTPS'] = int(input('Número da carteira de trabalho (digite [0] se não possui): '))
if dados['CTPS'] > 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    tempoServ = atual - dados['contratação']
    retired = (35 - tempoServ) + dados['idade']
print('*' * 40)
print(f'Nome: {dados["nome"]}')
print(f'Idade: {dados["idade"]} anos')
print(f'Nº da CTPS: {dados["CTPS"]}')
if dados['CTPS'] > 0:
    print(f'Ano de contratação: {dados["contratação"]}')
    print(f'Salário: {dados["salario"]}')
    print(f'Esse trabalhador vai se aposentar com {retired} anos.')
    