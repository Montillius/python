from curses import endwin
from queue import Empty
import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")


print("Será sorteado um número, entre o intervalo escolhido!")
print("*********************************")
n1_str = input("Digite o primeiro número: ")
print("*********************************")
n2_str = input("Digite o segundo número: ")
print("*********************************")
n1 = int(n1_str)
n2 = int(n2_str)
if(n1 > n2):
    print("O número escolhido estará entre ", n2, "e", n1)
    numero_random = random.randint(n2, n1)
elif(n2 > n1):
    print("O número escolhido estará entre ", n1, "e", n2)
    numero_random = random.randint(n1, n2)
else:
    print("Os números não podem ser iguais")

print("*********************************")
tentativa = input("Digite sua tentativa: ")
chute = int(tentativa)
if(tentativa == ""):
    print("Você não colocou nenhum número", "\n", "Fim do jogo")
    print("*********************************")
else:
    while (chute != numero_random):
        tentativa = input("Digite sua tentativa: ")
        chute = int(tentativa)
        if(tentativa == ""):
            print("Você não colocou nenhum número", "\n", "Fim do jogo")
    if(chute == numero_random):
        print("Você chutou", chute, "e acertou o número gerado foi ",
              numero_random, "Parabéns")
        print("Fim do jogo")
    else:
        print("Você errou o número gerado foi ",
              numero_random, " E você chutou ", chute)
        print("Fim do jogo!")

print("*********************************")
