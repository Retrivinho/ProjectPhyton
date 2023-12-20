print('CÁLCULO DE MÉDIA ANUAL DE ALUNO:')
print('=' * 31)
n1 = float(input('Digite a nota do 1º bimestre: '))
n2 = float(input('Digite a nota do 2º bimestre: '))
n3 = float(input('Digite a nota do 3º bimestre: '))
n4 = float(input('Digite a nota do 4° bimestre: '))
m = (n1 + n2 + n3 + n4) / 4
print('Sua média foi: {:.2f}'.format(m))
if m >= 6.0:
    print('Sua média foi BOA ! Parabéns ! Você foi APROVADO !')
else:
    print('Sua nota foi RUIM ! Você foi REPROVADO !')



