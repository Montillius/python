import random
import sys

def jogar():
    
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    rodada = 1
    total_de_tentativas = 0
    pontos = 1000
    numeros_chutados = []

    print("Será sorteado um número inteiro, entre o intervalo escolhido!", "\n",
        "lembre-se que não podem ser números iguais!")
    print("*********************************")
    n1 = int(input("Digite o menor valor: "))
    print("*********************************")
    n2 = int(input("Digite o maior valor: "))
    print("*********************************")

    if(n2 > n1):
        print("O número escolhido estará entre {} e {}".format(n1, n2))
        numero_secreto = random.randint(n1, n2)
    else:
        print("O intervao tem que ser informado com menor e maior valor nesta ordem!")
        print("****** Fim do jogo ******")
        sys.exit()
    print("*********************************")

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
        
    while (rodada <= total_de_tentativas):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = int(input("Digite o seu número: "))
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
            print("Game Over, O numero secreto era {} \n ".format(numero_secreto))
            print("*********************************")
            break
        elif(acertou):
            numeros_chutados.append(chute)
            print("Parabéns! Você acertou! O número secreto era {} \n E esses foram seus chutes {}".format(
                numero_secreto, numeros_chutados))
            print("*********************************")
            break
        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto!")
                print("*********************************")
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
                print("*********************************")

        numeros_chutados.append(chute)
    rodada = rodada + 1
    
if(__name__ == "__main__"):
    jogar()