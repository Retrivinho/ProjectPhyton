print('ALISTAMENTO MILITAR')
print('=-' * 10)
from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano de nascimento ? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}. '.format(nasc, idade, atual))
if idade == 18:
    print('Você completou 18 anos e deve se alistar no serviço militar IMEDIATAMENTE ! ')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não completou 18 anos e aida faltam {} anos para o alistamento. '.format(saldo))
    ano = atual + saldo
    print('O seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos. '.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}. Se você se alistou, está em dia com o Ministério do Exército Brasileiro !' .format(ano))











