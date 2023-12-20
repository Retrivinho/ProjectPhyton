print('TABUADA DE UM NÚMERO SOLICITADO')
print('=-' * 16)
num = int(input('Digite um número para ver a sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))

