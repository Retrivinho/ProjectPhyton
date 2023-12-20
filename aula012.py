print('NOMES:')
print('=-' * 15)
nome = str(input('Qual é o seu nome ? '))
if nome == 'Reginaldo':
    print('Que nome bonito ! ')
elif nome == 'Pedro' or nome == 'Silvia' or nome == 'Mário':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Sueli Cláudia Marlene Juliana Márcia Luciani':
    print('Belo nome feminino !')
else:
    print('Seu nome é bem comum !')
print('Tenha um bom dia, {} !'.format(nome))





