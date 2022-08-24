
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}". format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
<<<<<<< HEAD
        
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))
        
    def deposita(self, valor):
        self.saldo += valor
        
    def sacar(self, valor):
        self.saldo -= valor
    
=======

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))
>>>>>>> 810dbdc414ff7bebb5e5496f5782992871fae5c9
