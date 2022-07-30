import sys
import forca
import adivinha

def escolhe_jogo():
    print("*********************************")
    print("******Ecolha o seu jogo**********")
    print("*********************************")

    print("Forca       - (1)\nAdivinhação - (2)")
    print("*********************************")

    jogo = int(input("Qual jogo? "))

    if(jogo ==1):
        print("Jogando forca...")
        forca.jogar()
    elif(jogo ==2):
        print("Jogando adivinhação...")
        adivinha.jogar()
    else:
        print("Valor invalido")
        print("*********************************")
        sys.exit()

if(__name__ == "__main__"):
    escolhe_jogo()