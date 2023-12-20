print('ANALIZADOR DE ANO BISSEXTO')
print('-=' * 15)
from datetime import date
ano = int(input('Que ano você quer analisar ? Coloque o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {} é BISSEXTO'.format(ano))

