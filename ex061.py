print('GERADOR DE PA ')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão de PA: '))
termo = primeiro
cont = 1
while cont <= 20:
    print('{} → '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')



