# forca.py
import random


def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    acertou = False
    enforcou = False
    erros = 0

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(arquivo)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)

    while (not acertou and not enforcou):
        chute = input("Qual letra?")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                    index += 1
        else:
            erros += 1

        if(erros == 6):
            break
        if("_" not in palavra_secreta):
            break

        print(letras_acertadas)


    if("_" not in letras_acertadas):
        print("Você ganhou!")
    else:
        print("Você perdeu!")


    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()

