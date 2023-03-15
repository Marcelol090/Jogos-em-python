import random

# Use a breakpoint in the code line below to debug your script.
# Formatação 0 é para colocar um 0 antes da data e o 2 são as casas e o d é o tipo de dado

print("{:02d}/{:02d}/{:02d}".format(9, 3, 2023))
print("")


def jogar():
    print("********************************")
    print("Bem vindo no jogo de advinhação")  # Press Ctrl+F8 to toggle the breakpoint.
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível:"))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f'Tentativa {rodada} de {total_de_tentativas}')  # f-strings
        chute = int(input("Digite um número entre 1 e 100"))
        print("Você digitou", chute)

        if (chute < 1 or chute > 100):
            print("Você deve chutar um numero entre 1 e 5")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Seu chute foi maior do que o esperado")
            elif (menor):
                print("Seu numero foi menor do que o esperado")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()