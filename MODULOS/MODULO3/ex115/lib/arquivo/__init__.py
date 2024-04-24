from ex115.lib.interface import *


def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()

    except FileNotFoundError:
        return False

    else:
        return True


def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('ERRO na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerArquivo(nome):
    arquivo = 0
    try:
        arquivo = open(nome, 'rt')
    except:
        print('ERRO na leitura do arquivo.')
    else:
        cabecalho('Pessoas cadastradas:')
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        arquivo.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Ocorreu um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Ocorreu um ERRO ao escrever os dados!')
        else:
            print('Adicionado com sucesso!')
            a.close()
