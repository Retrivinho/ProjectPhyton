print("LISTA DE NUMEROS PARES E IMPARES:")
print("-=" * 16)
num = list()
pares = list()
impares = list()
while True:
    num.append(int(input("Digite um numero:  ")))
    resp = str(input("Quer continuar ? [S/N]" ))
    if resp in "Nn":
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append (v)
    elif v % 2 ==1:
        impares.append(v)
print("-=" * 25)
print(f"A lita completa é {num}.")
print(f"A lista de numeros pares é {pares}.")
print(f"A listade numeros impares é {impares}.")
print("-=" * 25)
print("FIM !")
