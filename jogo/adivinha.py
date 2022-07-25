import random
import os
import sys

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

cur = dir(os)
tentativas = 1
numeros_tentados = []

print("Será sorteado um número inteiro, entre o intervalo escolhido!", "\n",
      "lembre-se que não podem ser números iguais")
print("*********************************")
n1 = int(input("Digite o primeiro número: "))
print("*********************************")
n2 = int(input("Digite o segundo número: "))
print("*********************************")

if(n1 > n2):
    print("O número escolhido estará entre ", n2, "e", n1)
    numero_random = random.randint(n2, n1)
elif(n2 > n1):
    print("O número escolhido estará entre ", n1, "e", n2)
    numero_random = random.randint(n1, n2)
else:
    print("Os números não podem ser iguais")
    print("****** Fim do jogo ******")
    sys.exit()
print("*********************************")

chute = int(input("Digite sua tentativa: "))
numeros_tentados.append(chute)

print("*********************************")
while (chute != numero_random):
    tentativas += 1
    if (chute < numero_random):
        print("Você errou, Está é a", tentativas,
            "º tentativa", "\n", "Tente novamente, com um número maior")
    else:
        print("Você errou, Está é a", tentativas,
            "º tentativa", "\n", "Tente novamente, com um número menor")
    chute = int(input("Digite sua palpite: "))
    numeros_tentados.append(chute)
    print("*********************************")
if(chute == numero_random):
    print("Você chutou o numero", chute, "e acertou!!", "\n"
          "*****o número gerado foi ", numero_random, "*****")
    if (tentativas == 1):
        print("*****Você acertou de primeira****")
    else:
        print("Só foram ", tentativas, "tentativas, Parabéns!")
        print("Seus chutes foram ", numeros_tentados)
    print("*********************************")
    print("********** Fim do jogo **********")

print("*********************************")