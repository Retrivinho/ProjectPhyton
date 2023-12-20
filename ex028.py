from random import randint
computador = randint(0, 5)# faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar... ')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei ? '))#jogador tenta adivinhar
if jogador == computador:
    print('Parabésns ! Você conseguiu me vencer ! ')
else:
    print('Ganhei ! Eu pensei no número {} e não no {} !'.format(computador, jogador))
