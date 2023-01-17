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
        self.__saldo -= valor

    def transferencia(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)