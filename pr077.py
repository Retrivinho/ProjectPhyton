palavras = ('aprender', 'suportar', 'arrepender', 'preparar', 'suspender', 'arrepiar', 'apagar', 'corrigir', 'estender',
           'esplêndido', 'carregar', 'estúpido', 'sorrir', 'silêncio' )
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos : ', end='')
    for letra in p:
        if letra.lower() in 'aáâãeéêiíoóuú':
            print(letra, end="")
