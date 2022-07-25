import random
import os


print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

cur = dir(os)
tentativas = 1

print("Será sorteado um número, entre o intervalo escolhido!")
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

print("*********************************")

chute = int(input("Digite sua tentativa: "))
print("*********************************")
while (chute != numero_random):
    tentativas += 1
    print("Você errou, Está é a", tentativas,
          "º tentativa", "\n", "Tente novamente")
    chute = int(input("Digite sua palpite: "))
    print("*********************************")
if(chute == numero_random):
    print("Você chutou o numero", chute, "e acertou!!", "\n"
          "o número gerado foi ", numero_random, "Parabéns")
    if (tentativas == 1):
        print("Você acertou de primeira")
    else:
        print("Só foram ", tentativas, "tentativas")
    print("Fim do jogo")

print("*********************************")
