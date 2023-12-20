print('CONVERSOR DE MOEDA REAL / DÓLAR: ')
print('>' * 45)
real = float(input('Quanto dinheiro vocè tem na carteira ? R$ '))
dolar = real / 5.29
print('Com  R$ {:.2f} você pode comprar US$ {:.2f}'.format(real, dolar))

