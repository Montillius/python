import random
import sys


def jogar():

    imprime_mensagem_inicio()

    rodada = 1
    total_de_tentativas = 0
    pontos = 1000
    numeros_chutados = []

    n1 = menor_valor()
    n2 = maior_valor()
    numero_secreto = define_intervalo(n2, n1)
    total_de_tentativas = escolha_do_nivel()

    while (rodada <= total_de_tentativas):
        print("*********************************")
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = pede_chute()

        print("Você digitou ", chute)
        if((chute < n1) or (chute > n2)):
            print("Você deve digitar um número válido")
            rodada = rodada + 1
            continue
        print("*********************************")

        acertou = chute == numero_secreto
        errou = ((rodada == total_de_tentativas) and (chute != numero_secreto))
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(errou):
            imprime_mensagem_perdedor(numero_secreto)
            break
        elif(acertou):
            imprime_mensagem_vencedor(chute, numero_secreto, numeros_chutados)
            break
        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto!")
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")

        numeros_chutados.append(chute)
        rodada = rodada + 1


def imprime_mensagem_inicio():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")


def menor_valor():
    print("Será sorteado um número inteiro, entre o intervalo escolhido!", "\nlembre-se que não podem ser números iguais!")
    print("*********************************")
    n1 = int(input("Digite o menor valor: "))
    print("*********************************")
    return n1


def maior_valor():
    n2 = int(input("Digite o maior valor: "))
    print("*********************************")
    return n2


def define_intervalo(n2, n1):
    if(n2 > n1):
        print("O número escolhido estará entre {} e {}".format(n1, n2))
        print("*********************************")
        numero_secreto = random.randint(n1, n2)
        return numero_secreto
    else:
        print("O intervao tem que ser informado com menor e maior valor nesta ordem!")
        print("****** Fim do jogo ******")
        sys.exit()


def escolha_do_nivel():
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    return total_de_tentativas


def pede_chute():
    chute = int(input("Digite o seu número: "))
    return chute


def imprime_mensagem_vencedor(chute, numero_secreto, numeros_chutados):
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    numeros_chutados.append(chute)
    print("O número secreto era {} \nE esses foram seus chutes {}".format(
        numero_secreto, numeros_chutados))
    print("*********************************")


def imprime_mensagem_perdedor(numero_secreto):
    print("Game Over!")
    print("O numero secreto era {} \n ".format(numero_secreto))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if(__name__ == "__main__"):
    jogar()
