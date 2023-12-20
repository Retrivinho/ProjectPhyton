distância = float(input('Qual é a distancia da sua viajem ? '))
print('Você está prestes a começar uma viajem de {} Km.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R$ {:.2f}'.format(preço))
