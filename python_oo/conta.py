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

    def pode_sacar(self):
        pass

    def sacar(self, valor):
        if(self.pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print('O valor {} passou o limte'.format(valor))

    # O self serve para chamar métodos ou atributos
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite