print("TEMPO DE VIAGEM ")
print('=-' * 8)
def calcular_tempo_viagem(distancia, velocidade_media):
    # Verificar se a velocidade média é maior que zero para evitar divisão por zero

    if velocidade_media > 0:
        tempo = distancia / velocidade_media
        return tempo
    else:
        return "A velocidade média deve ser maior que zero."

try:
    # Obter entrada do usuário para a distância e a velocidade média :

    distancia = float(input("Digite a distância da viagem em quilômetros: "))
    velocidade_media = float(input("Digite a velocidade média em Km/h: "))

    # Calcula o tempo de viagem :

    tempo_viagem = calcular_tempo_viagem(distancia, velocidade_media)

    # Exibi o resultado :

    if isinstance(tempo_viagem, str):
        print(tempo_viagem)
    else:
        print(f"O tempo médio de viagem é de {tempo_viagem:.2f} horas.")
except ValueError:
    print("Por favor, insira números válidos para a distância e a velocidade média.")
