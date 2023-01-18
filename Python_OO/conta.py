class Conta:
    def __init__(self, numero, titular, saldo, limite):  # Função construtora
        print("")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo da conta é R${}".format(self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= (self.__saldo + self.__limite):
            self.__saldo -= valor

    def transferencia(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def titular(self):
        return self.__titular
    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite