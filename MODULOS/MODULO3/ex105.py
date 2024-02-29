def notas(*notas, sit=False):
    """_summary_Função para analisar notas e situação de vários alunos

    Args:
        notas (float): _uma ou mais notas do aluno_.
        sit (bool, optional): _situação do aluno_. Defaults to False.

    Returns:
        _type_: _dicionário com várias informações sobre a situação do aluno_
    """
    
    nota = {}
    nota['total'] = len(notas)
    nota['maior'] = max(notas)
    nota['menor'] = min(notas)
    nota['media'] = sum(notas) / len(notas)

    if sit:
        if nota['media'] <= 5:
            nota['situação'] = 'RUIM'
        elif nota['media'] > 5 and nota['media'] < 7:
            nota['situação'] = 'RAZOÁVEL'
        elif nota['media'] > 7:
            nota['situação'] = 'ÓTIMA'
    return nota
        

val = notas(5, 6, 4, 7.5, 3.5, 8,  sit=True)
print(val)
help(notas)