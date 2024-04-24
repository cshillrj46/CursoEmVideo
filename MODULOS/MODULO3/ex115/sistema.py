from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arquivo = 'cursoemvideo.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

cabecalho('Sistema de arquivos v1.0')
while True:
    resposta = menu(['Pessoas cadastradas', 'Cadastrar pessoa', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arquivo)
    elif resposta == 2:
        cabecalho('Novo cadastro')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema...')
        break
    else:
        print('\033[31mErro! Digite opção válida.\033[m')
    sleep(2)
