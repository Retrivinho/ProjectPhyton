print('CONVERSOR DE NÚMERO INTEIRO PARA BINÁRIO:')
print('=-' * 25)

num = int(input('Digite um número inteiro: '))
print( '''Escolha uma das bases de conversãa:
[ 1 ] cnverter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: ' ))
if opção == 1:
    print(' {} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print(' {} convretido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print(' {} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente !')


