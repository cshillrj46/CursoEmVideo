
def leiaDinheiro(msg):
    valid = False
    while not valid:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO! \"{entrada}\" é um valor inválido!')
        else:
            valid = True
            return float(entrada)