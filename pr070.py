print('ESTATÍSCA EM PRODUTOS:')
print('-=' * 12)
total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Mome do Produto:  '))
    preço = float(input('Preço: R$  '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
       menor = preço
       barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ?  [S/N]  ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print('O total da compra foi {:.2f}'.format(total))
print('Temos {} produtos custando mais de R$ 1.000.00 '.format(totmil))
print('O produto mais barato foi {} que custa R$ {:.2f}'.format(barato, menor))








