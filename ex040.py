print('Média Bimestral')
print('=' * 15)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}. '.format(n1, n2, média))
if 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO ! ')
elif média < 5:
    print('O aluno está REPROVADO ! ')
elif média >= 7:
    print('O aluno está APROVADO ! PARABÉNS ! '.format(média))


    





