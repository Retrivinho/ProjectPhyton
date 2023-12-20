print('=' * 30)
print('SIMULADOR DE CAIXA ELETRÔNICO:')
print('=' * 30)
valor = int(input('VALOR A SACAR: R$  '))
total = valor
céd = 200
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print('Total de {} cédulas de R$ {}'.format(totcéd, céd))
        elif céd == 200:
            céd = 100
        elif céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('>' * 55)
print('O BANCO AGRADECE ! OBRIGADO POR UTILIZAR O NOSSO CAIXA !')


