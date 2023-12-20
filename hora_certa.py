print('HORA CERTA')
print('=-' * 7)
entrada = input('Digite a hora em numeros inteiros : ')

try:
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
        print('BOM DIA !')
    elif hora >= 12 and hora <= 17:
        print('BOA TARDE !')
    elif hora >= 18 and hora <= 23:
        print('BOA NOITE !')
    else:
        print('NÃO CONHEÇO ESSE HORÁRIO !')
except:
    print('POR FAVOR, DIGITE APENAS NÚMROS INTEIROS !')
