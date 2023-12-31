nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Sua média é {} e você ficou \033[1;31mREPROVADO\033[m.'.format(media))
elif media <= 6.9:
    print('Sua média é {} e você ficou em \033[1;34mRECUPERAÇÃO\033[m.'.format(media))
else:
    print('Sua média é {} e você foi \033[1;33mAPROVADO\033[m.'.format(media))
    