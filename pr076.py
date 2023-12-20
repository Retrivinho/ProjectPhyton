print('LISTA DE PREÇOS DE MATERIAL ESCOLAR')
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.80,
            'Estojo', 5.50,
            'Régua', 4,
            'Compasso', 15.60,
            'Mochila', 140.70,
            'Caneta azul', 3,
            'Caneta vermelha', 3,
            'Caneta preta', 3,
            'Lapiseira', 20,
            'Livro', 35.80,
            'Grafite 0.5 mm', 0.50)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem [pos]:.<30}', end=' ')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)




