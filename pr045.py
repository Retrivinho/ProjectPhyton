from random import randint
ítens = ('Pedra', 'Papel' , 'Tesoura' )
computador = randint (0, 2)
print('''Suas opções:
[ 0 ] PERDA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada ? '))
print('-=' * 11)
print('Computador jogou {}'.format(ítens[computador]))
print('O jogador jogou {}'.format(ítens[jogador]))
print('-=' * 11)
if computador == 0: # coputador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('O JOGADOR VENCEU !')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU !')
    else:
        print('JOGADA INVÁLIDA !')
elif computador == 1: # O Computador jogou PAPEL
    if jogador == 0:
        print('O COMPUTADOR VENCEU !')
    elif jogador == 1:
        print('EMPATE !')
    elif jogador == 2:
        print('O JOGADOR VENCEU !')
    else:
        print('JOGADA INVÁLIDA !')
elif computador == 2: # O computador jogou TESOURA
    if jogador == 0:
         print('O JOGADOR VENCEU !')
    elif jogador == 1:
         print('O COMPUTADOR VENCEU !')
    elif jogador == 2:
         print('EMPATE !')
    else:
         print('JOGADA INVÁLIDA !')







