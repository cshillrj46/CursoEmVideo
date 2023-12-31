num = int(input('Digite um número inteiro qualquer: '))
print('Se deseja converter para BINÁRIO, digite [1]: ')
print('Se deseja converter para OCTAL, digite [2]: ')
print('Se deseja converter para HEXADECIMAL, digite [3]: ')
choice = int(input('Sua opção: '))
if choice == 1:
    print('Em BINÁRIO é: {}'.format(bin(num)[2:]))
elif choice == 2:
    print('Em OCTAL é: {}'.format(oct(num)[2:]))
elif choice == 3:
    print('Em HEXADECIMAL é: {}'.format(hex(num)[2:]))
else:
    print('Você digitou a opção errada.')
    
    

