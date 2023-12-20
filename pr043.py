print('CÁLCULO DE I.M.C.:')
print('=' * 30)
peso = float(input('Qual é o seu peso ? '))
altura = float(input('Qual é a sua altura ? '))
imc = peso / (altura ** 2)
print('O seu IMC é {:.1f} .'.format(imc))
if imc < 18.5:
    print('VOCÊ ESTÁ ABAIXO DO PESO IDEAL !')
elif 18.5 <= imc < 25:
    print('PESO IDEAL ! PARABÉNS, CONTINUE ASSIM ! ')
elif 25 <= imc < 30:
    print('SOBREPESO ! ')
elif 30 <= imc <= 40:
    print('OBESIDADE ! ')
elif imc >= 40:
    print('OBESIDADE MÓRBIDA ! CUIDADO !')
    


    






