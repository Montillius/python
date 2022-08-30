class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}". format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    # O self serve para chamar métodos ou atributos
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        
    def get_saldo(self):
        return self.__saldo 
    
    def get_titular(self):
        return self.__titular
    
    def set_titular(self, titular):
        self.__titular = titular
    
    def get_limite(self):
        return self.__limite
    
    def set_limite(self, limite):
        self.__limite = limite