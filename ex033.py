a = int(input('Insira o primeiro valor: '))
b = int(input('Insira o segundo valor: '))
c = int(input('Insira o terceiro valor '))
if a<b and a<c:
    menor = a
if b<c and c<a:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor  valor digitado foi {}'.format(menor))
print('O maior valor digitdo foi {}'.format(maior))

