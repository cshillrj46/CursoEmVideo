from datetime import date

def voto(num=0):
    atual = date.today().year
    num = atual - ano
    if num < 16:
        return(f'Com {num} anos. VOTO NEGADO')
    elif num >= 18 and num <= 65:
        return(f'Com {num} anos. VOTO OBRIGATÓRIO')
    else:
        return(f'Com {num} anos. VOTO OPCIONAL')


ano = int(input('Informe o ano de nascimento: '))
print(f'{voto(ano)}')
