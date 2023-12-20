print("CALCULADORA +, -, *, / ")
print("=-" * 10)
def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Não é possível dividir por zero."

# Função principal da calculadora
def calculadora():
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite o número da operação desejada (1/2/3/4): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print(num1, "+", num2, "=", soma(num1, num2))

    elif escolha == '2':
        print(num1, "-", num2, "=", subtracao(num1, num2))

    elif escolha == '3':
        print(num1, "*", num2, "=", multiplicacao(num1, num2))

    elif escolha == '4':
        print(num1, "/", num2, "=", divisao(num1, num2))

    elif escolha == '5':
        print("Escolha inválida")

    else:
        print("Escolha inválida")

# Chamar a função da calculadora
calculadora()

